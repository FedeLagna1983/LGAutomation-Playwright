Feature: Verificacion de contenidos principales en Home
  Como usuario del sitio
  Quiero validar los textos clave del Home
  Para confirmar que la informacion principal se despliega correctamente

  @homenavigation @bdd @e2e
  Scenario: Verificar textos clave del Home con scroll
    Given que el usuario abre la pagina Home para validar contenidos
    Then debe ver el texto "Welcome to the Future of TV Advertising"
    Then debe ver el texto "Connect to the LG Universe With Our AI-Powered Advertising Platform"
    Then debe ver el texto "A Winning Combination of Global Scale & Unique Reach"
    Then debe ver el texto "Everything You Need to Win with Connected TV"
    Then debe ver el texto "With LG Ad Solutions, advertisers now have a source for LG CTV inventory with one-stop planning, activation and measurement across all viewing platforms"
    Then debe ver el texto "Latest research & insights for better CTV media strategies"
    Then debe cerrar el navegador
