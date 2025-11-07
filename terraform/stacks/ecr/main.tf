# This can be improved by using a for_each loop if the number of repositories increases
module "blacklist_repository" {
  source = "../../modules/ecr"
  keep_tags_number = var.keep_tags_number
  repository_name  = var.blacklist_repository_name
}
