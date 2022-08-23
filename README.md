## Requirements
- Ubuntu OS
- Chrome driver
```bash
apt-get install chromium-driver
```

## Installation
- Use the project inside Python virtaulenv
- Install the requirements

```bash
pip install -r requirements.txt
```

## Deployment
- Inside the project please run

```bash
flask --app base run
```

- Navigate to `<baseurl>/deltas/<id>` to get the delta value, where `id` is the **BTCUSD** value, ex: `<baseurl>/deltas/BTCUSD-50000-P`
