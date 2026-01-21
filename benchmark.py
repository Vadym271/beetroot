import httpx
import asyncio
import time

BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = f"{BASE_URL}/accounts/login/"
ENDPOINTS = {
    "List Notes": f"{BASE_URL}/",
    "Create Note": f"{BASE_URL}/create_note/",
    "Update Note": f"{BASE_URL}/6/update/",
}

USER_DATA = {
    "username": "testuser",
    "password": "testpassword123"
}


async def run_benchmark():
    total_start_time = time.perf_counter()
    results = {}

    async with httpx.AsyncClient(follow_redirects=True) as client:

        await client.get(LOGIN_URL)

        login_data = {
            **USER_DATA,
            "csrfmiddlewaretoken": client.cookies.get("csrftoken"),
        }

        login_res = await client.post(LOGIN_URL, data=login_data)

        print(f"Login Status: {login_res.status_code}")

        if login_res.status_code != 200 or "Invalid" in login_res.text:
            print("Помилка авторизації. Перевірте дані.")
            return

        for name, url in ENDPOINTS.items():
            start = time.perf_counter()
            response = await client.get(url)
            end = time.perf_counter()

            results[name] = {
                "duration": f"{end - start:.4f}s",
                "status": response.status_code
            }

    total_duration = time.perf_counter() - total_start_time
    print(f"Загальний час виконання: {total_duration:.4f} секунд")


if __name__ == "__main__":
    asyncio.run(run_benchmark())