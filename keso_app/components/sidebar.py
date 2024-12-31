import reflex as rx
from .. import styles
from ..states import routes

def sidebar_item(text: str, 
                 icon: str, 
                 href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )

def icon_link(icon: str, 
              href: str) -> rx.Component:
    return rx.link(
        rx.icon_button(
            rx.icon(icon),
            size="2",
            variant="ghost",
            color_scheme="gray",
        ),
        href=href
    )

def account(fullname: str,
            username: str) -> rx.Component:
    return rx.hstack(
        rx.icon_button(
            rx.icon("user"),
            size="3",
            radius="full",
        ),
        rx.vstack(
            rx.box(
                rx.text(
                    fullname,
                    size="3",
                    weight="bold",
                ),
                rx.text(
                    username,
                    size="2",
                    weight="medium",
                ),
                width="100%",
            ),
            spacing="0",
            justify="start",
            width="100%",
        )
    )

def sidebar_bottom() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text("Ayuda", size="3"),
            href=routes.HELP_ROUTE,
            color_scheme="gray",
            underline="none",
        ),
        rx.link(
            rx.text("Contacto", size="3"),
            href=routes.CONTACT_ROUTE,
            color_scheme="gray",
            underline="none",
        ),
        rx.spacer(),
        rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
        justify="start",
        align="center",
        width="100%",
        padding="0.35em",
    )

def sidebar_profile_settings() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            account(
                "My account", 
                "user@reflex.dev"
                ),
            rx.spacer(),
            icon_link(
                "settings", 
                routes.SETTINGS_ROUTE
                ),
            padding_x="0.5rem",
            align="center",
            width="100%",
        )
    )

def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Resumen", "layout-dashboard", routes.HOME_ROUTE),
        sidebar_item("Producción", "milk", routes.PRODUCTION_ROUTE),
        sidebar_item("Ganado", "paw-print", routes.CATTLE_ROUTE),
        sidebar_item("Transacciones", "clipboard-pen-line", routes.TRANSACTIONS_ROUTE),
        sidebar_item("Registros", "notebook-tabs", routes.SYSTEM_LOGS_ROUTE),
        spacing="1",
        width="100%",
    )

def sidebar_desktop() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="/logo.svg",
                width="2.25em",
                height="auto",
                border_radius="25%",
            ),
            rx.heading(
                "Keso", size="7", weight="bold"
            ),
            align="center",
            justify="start",
            padding_x="0.5rem",
            width="100%",
        ),
        sidebar_items(),
        rx.spacer(),
        rx.vstack(
            sidebar_profile_settings(),
            rx.divider(),
            sidebar_bottom(),
            width="100%",
            spacing="5",
        ),
        spacing="5",
        padding_x="1em",
        padding_y="1.5em",
        bg=rx.color("accent", 3),
        align="start",
        height="100dvh",
        width="16em",
    )

def sidebar_mobile() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon("align-justify", size=30)
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.box(
                        rx.drawer.close(
                            rx.icon("x", size=30)
                        ),
                        width="100%",
                    ),
                    sidebar_items(),
                    rx.spacer(),
                    rx.vstack(
                        sidebar_profile_settings(),
                        rx.divider(margin="0"),
                        sidebar_bottom(),
                        width="100%",
                        spacing="5",
                    ),
                    spacing="5",
                    width="100%",
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="1.5em",
                bg=rx.color("accent", 2),
            ),
            width="100%",
        ),
        direction="left",
    )

def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            sidebar_desktop()
        ),
        rx.mobile_and_tablet(
            sidebar_mobile(),
            padding="1em",
        ),
    )