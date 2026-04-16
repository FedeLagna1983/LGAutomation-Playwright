# LGAutomation Playwright

Proyecto de automatizacion web con Playwright + Pytest y soporte BDD con `pytest-bdd`.

## 1) Introduccion a BDD y como Pytest lo complementa

BDD (Behavior Driven Development) permite describir comportamiento de negocio con lenguaje natural (Gherkin):

- `Given` precondiciones
- `When` acciones
- `Then` resultados esperados

Pytest complementa BDD porque aporta:

- fixtures reutilizables (`page`, `home_page`, `base_url`)
- asserts y plugins maduros
- ejecucion simple desde terminal
- reportes y hooks (ej: screenshot en fallo)

En este repo:
- la capa Page Object Model vive en `pages/`
- los escenarios de negocio viven en `tests/features/*.feature`
- la implementacion tecnica de pasos vive en `tests/test_navigation_bdd.py`

## 2) Instalacion de plugin y dependencias

El plugin BDD es `pytest-bdd` (ya agregado a `requirements.txt`).

Instalar todo en tu entorno virtual:

```powershell
python -m pip install -r requirements.txt
python -m playwright install
```

## 3) Feature file en Gherkin

Archivo:

- `tests/features/navigation.feature`

Escenario implementado:
- abrir Home
- navegar a Contact desde el menu
- volver a Home desde el logo

## 4) Step definitions con Pytest-BDD

Archivo:

- `tests/test_navigation_bdd.py`

Buenas practicas aplicadas:

- cada step hace una sola responsabilidad
- se reutilizan los Page Objects existentes
- los pasos son legibles y cercanos al lenguaje de negocio
- la validacion tecnica queda en los metodos de pagina

## 5) Compartir datos entre steps

Se usa un fixture de contexto compartido:

- `bdd_context: dict[str, object]`

Ese diccionario guarda estado entre pasos del mismo escenario, por ejemplo:

- pagina home abierta
- pagina contact despues del click
- paths esperados para validaciones

## 6) Ejecutar tests BDD end-to-end

Ejecutar solo BDD:

```powershell
python -m pytest tests/test_navigation_bdd.py --headed --browser chromium -s
```

Ejecutar por tag para Jenkins:

```powershell
python -m pytest -m jenkins --browser chromium --junitxml=artifacts/reports/pytest-jenkins.xml
```

Ejecutar todo el proyecto (tests clasicos + BDD):

```powershell
python -m pytest --headed --browser chromium -s
```

Para verlo mas lento:

```powershell
python -m pytest --headed --browser chromium --slowmo 500 -s
```

## 7) Configuracion adicional del proyecto

- `BASE_URL` configurable por variable de entorno (default: `https://lgads.tv`)
- screenshots automaticos en `artifacts/screenshots/` cuando un test falla
- `.gitignore` para artefactos de Python y pruebas
