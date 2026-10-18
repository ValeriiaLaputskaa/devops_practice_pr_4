from molotov import scenario

@scenario(weight=100)
async def check_response(session):
    async with session.get("http://localhost:8080") as resp:
        assert resp.status == 200, f"Очікувався код 200, отримано {resp.status}"
        data = await resp.json()
        assert "status" in data, "У відповіді немає JSON"
