from fck_aws_sso.authorize_sso import authorize_sso
from fck_aws_sso.io import read_stdin_until_data_is_extracted
import typer


def main(headless: bool = True):
    extracted_url, extracted_code = read_stdin_until_data_is_extracted()
    authorize_sso(extracted_url, extracted_code, headless)


if __name__ == "__main__":
    typer.run(main)
