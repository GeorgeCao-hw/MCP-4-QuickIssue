# app/tools.py
from app.adapters.issues import query_issues


def list_tools():
    return {
        "tools": [
            {
                "name": "query_community_issues",
                "description": (
                    "Query community issues from openEuler QuickIssue system. "
                    "Supports filtering by organization, repository, SIG, state, "
                    "labels, assignee, priority, and full-text search."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "org": {
                            "type": "string",
                            "description": "Organization that the issue belongs to"
                        },
                        "repo": {
                            "type": "string",
                            "description": "Repository that the issue belongs to"
                        },
                        "sig": {
                            "type": "string",
                            "description": "SIG (Special Interest Group) name"
                        },

                        "state": {
                            "type": "string",
                            "description": (
                                "High-level issue state, e.g. open or closed"
                            )
                        },

                        "issue_state": {
                            "type": "string",
                            "description": (
                                "More specific issue state used by the backend "
                                "(optional, advanced usage)"
                            )
                        },

                        "type": {
                            "type": "string",
                            "description": "Issue type, e.g. bug, task, feature"
                        },

                        "priority": {
                            "type": "integer",
                            "description": "Issue priority level"
                        },

                        "author": {
                            "type": "string",
                            "description": "Issue author / creator"
                        },

                        "assignee": {
                            "type": "string",
                            "description": "User assigned to the issue"
                        },

                        "branch": {
                            "type": "string",
                            "description": "Target branch for the issue"
                        },

                        "label": {
                            "type": "string",
                            "description": "Label applied to the issue"
                        },

                        "exclude_label": {
                            "type": "string",
                            "description": "Label to be excluded from results"
                        },

                        "search": {
                            "type": "string",
                            "description": (
                                "Full-text search keyword, matching issue number, "
                                "repository name, or title"
                            )
                        },

                        "sort": {
                            "type": "string",
                            "description": (
                                "Sort field, default is created_at"
                            ),
                            "default": "created_at"
                        },

                        "direction": {
                            "type": "string",
                            "description": (
                                "Sort direction, default is desc"
                            ),
                            "enum": ["asc", "desc"],
                            "default": "desc"
                        },

                        "page": {
                            "type": "integer",
                            "description": "Page number, starting from 1",
                            "default": 1
                        },

                        "page_size": {
                            "type": "integer",
                            "description": (
                                "Number of issues per page (max 100)"
                            ),
                            "default": 10
                        }
                    },
                    "required": []
                }
            }
        ]
    }


def call_tool(name: str, arguments: dict):
    if name == "query_community_issues":
        return query_issues(arguments)

    raise ValueError(f"Unknown tool: {name}")


