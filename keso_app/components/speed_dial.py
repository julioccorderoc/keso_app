import reflex as rx

class SpeedDialMenu(rx.ComponentState):
    is_open: bool = False

    @rx.event
    def toggle(self, value: bool):
        self.is_open = value

    @classmethod
    def get_component(cls, **props):
        def menu_item(icon: str, text: str) -> rx.Component:
            return rx.hstack(
                rx.icon(icon, padding="2px"),
                rx.text(text, weight="medium"),
                align="center",
                opacity="0.75",
                cursor="pointer",
                position="relative",
                _hover={
                    "opacity": "1",
                },
                width="100%",
                align_items="center",
            )

        def menu() -> rx.Component:
            return rx.box(
                rx.card(
                    rx.vstack(
                        menu_item("milk", "Leche"),
                        rx.divider(margin="0"),
                        menu_item("package-plus", "Queso"),
                        rx.divider(margin="0"),
                        menu_item("circle-plus", "Ventas"),
                        rx.divider(margin="0"),
                        menu_item("circle-minus", "Gastos"),
                        direction="column-reverse",
                        align_items="end",
                        justify_content="end",
                    ),
                    box_shadow="0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)",
                ),
                position="absolute",
                bottom="100%",
                right="0",
                padding_bottom="10px",
            )

        return rx.box(
            rx.box(
                rx.icon_button(
                    rx.icon(
                        "plus",
                        style={
                            "transform": rx.cond(
                                cls.is_open,
                                "rotate(45deg)",
                                "rotate(0)",
                            ),
                            "transition": "transform 150ms cubic-bezier(0.4, 0, 0.2, 1)",
                        },
                        class_name="dial",
                    ),
                    variant="solid",
                    size="3",
                    cursor="pointer",
                    radius="full",
                    position="relative",
                ),
                rx.cond(
                    cls.is_open,
                    menu(),
                ),
                position="relative",
            ),
            on_mouse_enter=cls.toggle(True),
            on_mouse_leave=cls.toggle(False),
            on_click=cls.toggle(~cls.is_open),
            style={"bottom": "15px", "right": "15px"},
            position="absolute",
            # z_index="50",
            **props,
        )


# Create the component function
speed_dial_menu = SpeedDialMenu.create
def render_speed_dial() -> rx.Component:

    """Render the speed dial menu component.
    
    Returns:
        rx.Component: The speed dial menu component.

    """
    return rx.box(
        speed_dial_menu(),
        position="fixed",  # Changed to fixed to stay in viewport
        bottom="1.5em",
        right="1.5em",
        z_index="1000",
    )