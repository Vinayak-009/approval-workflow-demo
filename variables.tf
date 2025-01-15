# variables.tf
variable "instance_name" {
  description = "The name of the compute instance"
  type        = string
  default     = "terraform-vm"
}

variable "machine_type" {
  description = "The machine type to use for the instance"
  type        = string
  default     = "e2-micro"
}

variable "image" {
    description = "the image to use for the VM"
    type = string
    default = "debian-cloud/debian-11"
}

variable "zone" {
  description = "The GCP zone to deploy the instance in"
  type        = string
  default = "us-central1-a"
}