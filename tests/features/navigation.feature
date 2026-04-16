Feature: Navegacion principal de LG Ads
  Como usuario del sitio
  Quiero navegar entre Home y Contact
  Para confirmar que el menu y el logo funcionan correctamente

  @jenkins @bdd @e2e
  Scenario: Navegar de Home a Contact y volver a Home
    Given que el usuario abre la pagina Home
    When hace click en el enlace Contact del menu
    Then debe ver la pagina Contact
    When hace click en el logo de LG Ad Solutions
    Then debe volver a la pagina Home
