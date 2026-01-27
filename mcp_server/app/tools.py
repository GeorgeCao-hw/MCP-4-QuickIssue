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
                            "description": "Issue author / creator. Use this when user says 'X提交的/创建的'"
                        },

                        "assignee": {
                            "type": "string",
                            "description": "User assigned to the issue. Use this when user says '分配给X的 '"
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
                            "description": ("Number of issues per page (max 100)"),
                            "default": 10
                        },

                        "limit": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 50,
                            "default": 10,
                            "description": "Maximum number of issues to return. If user asks for N results, you MUST set limit=N."
                        },

                        "sort_by": {
                            "type": "string",
                            "enum": ["created_at", "updated_at"],
                            "default": "updated_at",
                            "description": "Sort field. 'latest' usually means updated_at unless user specifies created time."
                        },
                        "order": {
                            "type": "string",
                            "enum": ["asc", "desc"],
                            "default": "desc"
                        }

                    }

                },
                    "required": []
            }
        ]
    }


def call_tool(name: str, arguments: dict):
    if name == "query_community_issues":
        return query_issues(arguments)

    raise ValueError(f"Unknown tool: {name}")


