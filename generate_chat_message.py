import json
import sys
import os

def create_google_chat_message(terraform_plan_output, github_run_id, commit_message, terraform_changes):
    """Creates a Google Chat message with buttons and Terraform plan output."""

    # Format Terraform plan
    formatted_plan = terraform_plan_output
    if formatted_plan:
        formatted_plan = f"```\n{terraform_plan_output}\n```"
    else:
        formatted_plan = "No Terraform changes detected."
    
    formatted_changes = terraform_changes
    if formatted_changes:
         formatted_changes = f"```\n{formatted_changes}\n```"
    else:
        formatted_changes = "No Terraform changes detected."
    
    message = {
        "text": f"Terraform Apply Required for commit: {commit_message}\n* Plan:\n{formatted_plan}\n* Changes:\n{formatted_changes}\n Please approve or deny the deployment.",
        "cards": [
            {
                "header": {
                    "title": "Terraform Deployment Required"
                },
                "sections": [
                    {
                      "widgets":[
                          {
                            "buttons": [
                              {
                                 "textButton": {
                                  "text": "Approve",
                                   "onClick": {
                                     "action": {
                                          "function": "approve",
                                          "message_id": f"{github_run_id}"
                                       }
                                    }
                                 }
                              },
                              {
                                "textButton": {
                                  "text": "Deny",
                                  "onClick": {
                                     "action": {
                                          "function": "deny",
                                          "message_id": f"{github_run_id}"
                                       }
                                    }
                                  }
                                }
                            ]
                          }
                        ]
                    }
                ]
              }
        ]
    }
    return json.dumps(message)


if __name__ == "__main__":
    if len(sys.argv) < 4:
      print("Usage: python generate_chat_message.py <terraform_plan_output> <github_run_id> <commit_message> <terraform_changes>")
      sys.exit(1)
    terraform_plan = sys.argv[1]
    github_run_id = sys.argv[2]
    commit_message = sys.argv[3]
    terraform_changes = sys.argv[4]
    message = create_google_chat_message(terraform_plan, github_run_id, commit_message, terraform_changes)
    print(message) # Prints the JSON payload to standard output
