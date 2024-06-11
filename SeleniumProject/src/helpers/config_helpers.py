
import os
#from SeleniumProject.src.helpers.config_helpers import get_base_url
def get_base_url():



    env = os.environ.get('ENV', 'test')  # Added comma here
    if env.lower() == 'test':
        return 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    elif env.lower() == 'prod':
        return 'https://opensource-demo.prod.orangehrmlive.com/web/index.php/auth/login'
    else:
        raise Exception(f"Unknown environment: {env}")


base_url = get_base_url()
print(base_url)

