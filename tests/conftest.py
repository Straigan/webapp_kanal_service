from webapp import create_webapp
import pytest


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_webapp()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client