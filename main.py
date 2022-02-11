from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata

class RestTemplate(Template):

    def pre_hook(self, metadata: Metadata) -> Metadata:
        print("Ação anterior a criação do projeto...")
        # Poderia ser a criação de uma pasta com um path passado como input
        return metadata

    def post_hook(self, metadata: Metadata):
        print(f"Ação após criação do projeto {metadata.inputs['project_name']}...")
        # Poderia ser a instação de uma dependencia por exemplo:
        # self.cwd = os.getcwd()
        # os.chdir(metadata.target_path)
        # subprocess.run('npm install @types/aws-lambda @orangestack-cdk/openapi-lambda', shell=True)


if __name__ == '__main__':
  run(RestTemplate())
