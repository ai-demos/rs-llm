import json
from phi.agent.file import FileAgent
from phi.conversation import Conversation

from workspace.settings import ws_settings

file_agent = FileAgent(base_dir=ws_settings.ws_root.joinpath("api/wip"))
status_router_name = "status"
status_routes_spec = ws_settings.ws_root.joinpath("data/specs/status_routes.json").read_text()

conversation = Conversation(
    system_prompt="""\
    You are a FastApi expert and are helping a user generate FastApi routes using an OpenApi specification.
    This is an important task and the users success depends on it. It must be done correctly.
    You must follow these instructions carefully.

    <instructions>
    1. Provided an OpenApi specification, THINK STEP BY STEP about the routes you need to create.
    2. Once you have the routes, generate FastApi code to create the routes using the `template` below.
    3. Always complete the function implementation, including test data.
    4. After the code is ready, save it to a file using the `save_file` function. Name the file `router_name_routes.py`.
    5. Continue till you have accomplished the task.
    </instructions>

    <template>
    from fastapi import APIRouter

    ######################################################
    ## Router for router_name routes
    ######################################################

    router_name_router = APIRouter(tags=["router_name"])

    @router_name_router.get(/path)
    def function():
        <implement this function with test data>

    </template>
    """,
    agents=[file_agent],
    show_function_calls=True,
    function_call_limit=5,
    # debug_mode=True,
)

conversation.print_response(f"Router Name: {status_router_name}\n\n<OpenApi Specification>\n{status_routes_spec}\n<OpenApi Specification>", stream=False)
