0x18-webstack_monitoring

```To get the dashboard id from the given api use this:```
curl -X GET \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: YOUR_API_KEY" \
  -H "DD-APPLICATION-KEY: YOUR_APPLICATION_KEY" \
  "https://api.datadoghq.com/api/v1/dashboard"
