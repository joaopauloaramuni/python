from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask


def solvecaptcha(url: str, site_key: str) -> str:
    """
    Solve Captcha
    :param url:
    :param site_key:
    :return: solution response
    """
    api_key = "api_key_here"
    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key, is_invisible=True)
    job = client.createTask(task)
    job.join()
    return job.get_solution_response()
