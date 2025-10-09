# =====================
# VARIABLES GENERALES
# =====================
AWS_REGION=us-east-1
ACCOUNT_ID=387050840675

# Credenciales fijas para la base de datos
DB_USER=proyectogrupo10
DB_PASSWORD=proyectogrupo10

export AWS_REGION

# =====================
# STACKS INDIVIDUALES
# =====================
rds:
	cd terraform/stacks/rds && \
	terraform init -backend-config="../../environments/rds/backend.tfvars" && \
	terraform plan -var-file="../../environments/rds/terraform.tfvars" -out .tfplan && \
	terraform apply ".tfplan"

# =====================
# DESTROY
# =====================

destroy-rds:
	cd terraform/stacks/rds && \
	terraform destroy -var-file="../../environments/rds/terraform.tfvars"

# =====================
# WORKFLOWS COMPLETOS
# =====================

deploy: rds
destroy: destroy-rds
