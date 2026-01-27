# GET https://quickissue.openeuler.org/api-issues/issues

# app/adapters/issues.py
import requests

BASE_URL = "https://quickissue.openeuler.org"

DEFAULT_TIMEOUT = 8


def query_issues(args: dict):
    """
    Adapter for:
    GET /api-issues/issues

    This function maps MCP semantic arguments
    to QuickIssue API query parameters.
    """

    url = f"{BASE_URL}/api-issues/issues"
    params = {}

    # ---------- 基本归属 ----------
    if args.get("org"):
        params["org"] = args["org"]

    if args.get("repo"):
        params["repo"] = args["repo"]

    if args.get("sig"):
        params["sig"] = args["sig"]

    # ---------- 状态 & 类型 ----------
    # MCP 统一用 state
    if args.get("state"):
        params["state"] = args["state"]

    # issue 的更细状态（可选）
    if args.get("issue_state"):
        params["issue_state"] = args["issue_state"]

    if args.get("type"):
        params["issue_type"] = args["type"]

    if args.get("priority") is not None:
        params["priority"] = int(args["priority"])

    # ---------- 人员 ----------
    if args.get("author"):
        params["author"] = args["author"]

    if args.get("assignee"):
        params["assignee"] = args["assignee"]

    # ---------- 分支 ----------
    if args.get("branch"):
        params["branch"] = args["branch"]

    # ---------- 标签 ----------
    if args.get("label"):
        params["label"] = args["label"]

    if args.get("exclude_label"):
        params["exclusion"] = args["exclude_label"]

    # ---------- 搜索 ----------
    if args.get("search"):
        params["search"] = args["search"]

    # ---------- 排序 ----------
    params["sort"] = args.get("sort", "created_at")
    params["direction"] = args.get("direction", "desc")

    # ---------- 分页 ----------
    params["page"] = int(args.get("page", 1))

    # MCP 用 page_size，API 用 per_page
    page_size = int(args.get("page_size", 10))
    params["per_page"] = min(page_size, 100)

    # ---------- 请求 ----------
    try:
        resp = requests.get(url, params=params, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as e:
        return {
            "error": "quickissue_request_failed",
            "message": str(e),
            "params": params
        }

    try:
        return resp.json()
    except ValueError:
        return {
            "error": "invalid_json_response",
            "text": resp.text
        }


