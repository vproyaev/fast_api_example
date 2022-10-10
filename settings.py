import dotenv
import pydantic

dotenv.load_dotenv()


class Settings(pydantic.BaseSettings):
    external_server_port: int
    external_server_address: str

    internal_server_port: int
    internal_server_address: str

    local_files_root: str
    docker_files_root: str

    jwt_secret: str
    jwt_algorithm: str
    jwt_expiration: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = False


settings = Settings()
