import flet as ft

def main(page: ft.Page):
    page.title = "Two-View Greeting App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Shared variable to keep the entered name
    user_name = ""

    # Define the AlertDialog for validation when the name field is empty
    def close_dialog(e):
        page.close(dialog)
        page.update()

    dialog = ft.AlertDialog(
        title=ft.Text("Missing Information"),
        content=ft.Text("Please enter your name before continuing."),
        actions=[ft.TextButton("OK", on_click=close_dialog)],
    )

    # Route change handler to manage multiple views
    async def route_change(route):
        page.views.clear()

        # Home View (/)
        if page.route == "/":
            name_field = ft.TextField(
                label="Enter your name", 
                value=user_name,
                width=300
            )

            async def on_continue_click(e):
                nonlocal user_name
                # 2. Check if the name field is empty
                if not name_field.value.strip():
                    page.open(dialog)
                    page.update()
                    return
                
                # Save name to shared variable
                user_name = name_field.value.strip()
                
                # Navigate to greeting view
                await page.push_route("/greeting")

            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Text("Welcome!", size=24, weight=ft.FontWeight.BOLD),
                        name_field,
                        ft.ElevatedButton("Continue", on_click=on_continue_click),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        # Greeting View (/greeting)
        elif page.route == "/greeting":
            async def on_back_click(e):
                await page.push_route("/")

            page.views.append(
                ft.View(
                    "/greeting",
                    [
                        ft.Text(f"Hello, {user_name}!", size=28, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton("Back", on_click=on_back_click),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        page.update()

    async def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Initial route setup
    page.push_route("/")

# 3. Start the app as a web server on port 8000 for GitHub Codespaces
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER, host="0.0.0.0", port=8000)
