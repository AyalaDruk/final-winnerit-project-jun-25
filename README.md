🧪 Final Automation Project - Playwright & Python  
**A professional QA automation framework for UI & API testing with full Allure reporting and CI/CD integration.**


🌟 Features
✅ UI Automation using Playwright (Python)

✅ API Automation using Requests and Pytest

📂 Clean architecture with Page Object Model (POM)

📸 Allure Reports with:

Screenshots on failure

Videos for all UI test executions

Request/Response JSON attachments

🌐 Cross-browser testing: Chrome, Firefox, Safari

🔄 CI/CD ready with GitHub Actions workflows

🏗️ Project Structure
bash
Copy
Edit
final-winnerit-project-jun-25/
│
├── 📂 api_requests/          # API request generators
│   ├── request_generator.py  # Core API wrapper with Allure steps
│   └── users_request_generator.py
│
├── 📂 pages/                 # UI Page Object Model
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│
├── 📂 tests/                 # Test cases
│   ├── 📂 api/               # API tests for ReqRes
│   └── 📂 ui/                # UI tests for SauceDemo
│   └── conftest.py           # Fixtures and hooks
│
├── 📂 utils/                 # Utility functions
│   └── allure_utils.py       # Attach screenshots/videos
│
├── 📂 .github/workflows/     # CI/CD GitHub Actions
│   └── playwright.yml
│
├── 📄 pytest.ini             # Pytest config
├── 📄 requirements.txt       # Python dependencies
└── 📄 README.md               # This file
🔗 API Tests
The API tests cover the full ReqRes API:

✔ Endpoints Tested:

📥 GET /users – Fetch user list (pagination supported)

📤 POST /users – Create a new user

📝 PUT /users/:id – Update user data

✏️ PATCH /users/:id – Partial updates

❌ DELETE /users/:id – Delete user

⚠️ Error handling – Validate 404 for invalid resources

📝 Example API Test

python
Copy
Edit
@pytest.mark.api
def test_get_single_user(users_api):
    response = users_api.get_user(2)
    users_api.validate_status_code(response, 200)
    response_body = response.json()
    users_api.validate_json_key_values(
        response_body["data"],
        {
            "id": 2,
            "first_name": "Janet",
            "email": "janet.weaver@reqres.in"
        }
    )
🎨 UI Tests
The UI tests automate critical flows on SauceDemo:

✔ Scenarios Covered:

✅ Login success (multiple users)

❌ Login failure (invalid credentials)

🛒 Add products to cart

🛍️ Complete an order (End-to-End flow)

📝 Example UI Test

python
Copy
Edit
def test_login_standard_user_success(login_page, inventory_page):
    login_page.navigate()
    login_page.type_username("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_url_to_be(inventory_page.inventory_url)
📊 Allure Reports
Allure provides detailed reports including:

✅ Test steps with clear descriptions

📸 Screenshots for all UI/API failures

🎥 Videos of all UI tests (not only on failure)

📄 JSON Payloads: Request & Response attached

🚀 GitHub Actions CI/CD
This project includes a GitHub Actions workflow:

🛠 Automatically runs tests on each push and pull request

📥 Generates Allure reports and uploads them as artifacts

🛠 Technologies Used
Technology	Purpose	Version
🕹 Playwright	UI automation framework	1.53.0
🧪 Pytest	Test runner	8.4.1
🌐 Requests	API testing library	2.32.4
📊 Allure	Advanced reporting	2.14.3
🎭 Faker	Generate fake test data	24.7.1
🚀 GitHub Actions	CI/CD automation	-

🧪 Run Tests
Run all tests:

bash
Copy
Edit
pytest
Run UI tests:

bash
Copy
Edit
pytest tests/ui/
Run API tests:

bash
Copy
Edit
pytest tests/api/
Generate Allure report:

bash
Copy
Edit
pytest --alluredir=allure-results
allure serve allure-results
🌱 Future Improvements
🐳 Dockerize for environment consistency

🔄 Extend API edge case coverage

📱 Add mobile browser testing

👩‍💻 Author
Ayala Druk
📫 LinkedIn | GitHub