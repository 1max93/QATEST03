import pytest
import time
import logging
import allure
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from pages.checkboxes_page import CheckboxesPage

logger = logging.getLogger(__name__)

@allure.title("Test Fonctionnel : Authentification et Vérification de Checkboxes")
@allure.description("""
Scénario de test fonctionnel détaillé sur The Internet:

1. Connexion à la zone sécurisée via Form Authentication.
2. Vérification du message de succès et du header "Secure Area".
3. Retour à la page d'accueil.
4. Navigation vers la page 'Checkboxes'.
5. Vérification et action sur un checkbox.
""")
@pytest.mark.usefixtures("driver")
def test_complex_functional_scenario(driver):
    start_time = time.time()

    with allure.step("Étape 1: Ouverture de la page login et authentification"):
        login_page = LoginPage(driver)
        login_page.open()
        time.sleep(1)
        login_page.login("tomsmith", "SuperSecretPassword!")
        logger.info("   -> Login effectué avec 'tomsmith'")

    with allure.step("Étape 2: Vérification de l'accès à la zone sécurisée"):
        secure_area = SecureAreaPage(driver)
        time.sleep(1)
        heading = secure_area.get_heading()
        assert "Secure Area" in heading, "Échec: 'Secure Area' devrait être présent."
        logger.info("   -> 'Secure Area' détecté.")
        success_msg = secure_area.get_success_message()
        assert "You logged into a secure area!" in success_msg, "Échec: Message de succès non attendu."
        logger.info("   -> Message de succès affiché.")

    with allure.step("Étape 3: Retour à la page d'accueil"):
        driver.get("https://the-internet.herokuapp.com")
        time.sleep(1)
        logger.info("   -> Retour accueil effectué.")

    with allure.step("Étape 4: Navigation vers la page 'Checkboxes'"):
        checkboxes_page = CheckboxesPage(driver)
        checkboxes_page.open()
        time.sleep(1)
        logger.info("   -> Page Checkboxes chargée.")

    with allure.step("Étape 5: Vérification et action sur le premier checkbox"):
        is_checked = checkboxes_page.check_first_box_if_not_checked()
        assert is_checked, "Échec: Le premier checkbox devrait être coché après l'action."
        logger.info("   -> Le premier checkbox est maintenant coché.")

    total_duration = time.time() - start_time
    logger.info(f"Test terminé avec succès en {total_duration:.2f} secondes.")
