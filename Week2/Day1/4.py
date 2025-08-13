

# | Component    | Description                                                                                                   | Similar to (MVC)        |
# | ------------ | ------------------------------------------------------------------------------------------------------------- | ----------------------- |
# | **Model**    | Represents the **data structure**. Handles all the data-related logic (database tables, queries, etc).        | **Model**               |
# | **Template** | The **presentation layer** — it handles what the user sees. HTML + Django template language.                  | **View (in MVC)**       |
# | **View**     | The **business logic** layer. It processes user requests, interacts with models, and sends the response back. | **Controller (in MVC)** |


# Template:
#     it is a presenation layer.it contain html files.
#     it use dtl to dispaly dynamic content.
#     it can include variable and logic like loop and conditions


# view:
#     it is buisiness logic layer
#     common methods:
#         httpresponse
#         render
#         redirect
#     it Take req.
#     aplly buisness logic.
#     return response.
#     it send data to template for rendering