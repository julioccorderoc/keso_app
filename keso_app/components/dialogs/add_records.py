import reflex as rx


def trigger_button(
        button_text: str,
        icon: str = "plus",
    ) -> rx.Component:
    
    return rx.dialog.trigger(
            rx.button(
                rx.icon(
                    icon, 
                    size=26
                ),
                rx.text(
                    button_text, 
                    size="4", 
                    display=[
                        "none", 
                        "none", 
                        "block"
                    ]
                ),
                size="3",
            ),
    )
    
    
def action_buttons(
        on_close: callable, 
        on_submit: callable,
        submit_button_text: str,
        cancel_button_text: str = "Cancel",
    ) -> rx.Component:

    return rx.flex(
        rx.dialog.close(
            rx.button(
                cancel_button_text,
                variant="soft",
                color_scheme="gray",
                on_click=on_close,
            ),
        ),
        rx.button(
            submit_button_text, 
            on_click=on_submit
        ),
        padding_top="2em",
        spacing="3",
        mt="4",
        justify="end",
    )


def dialog_header(
        icon: str,
        title: str,
        description: str, 
    ) -> rx.Component:
    
    return rx.box(
        rx.hstack(
            rx.badge(
                rx.icon(
                    tag=icon, 
                    size=34
                ),
                radius="full",
                padding="0.65rem",
                ),
            rx.vstack(
                rx.dialog.title(
                    title,
                    weight="bold",
                    margin="0",
                ),
                rx.dialog.description(
                    description,
                ),
                spacing="1",
                height="100%",
                align_items="start",
            ),
            height="100%",
            spacing="4",
            margin_bottom="1.5em",
            align_items="center",
            width="100%",
        )    
    )



def dialog_actions(
        primary_button_text: str,
        secondary_button_text: str,
    ) -> rx.Component:
    
    return rx.box(
        rx.hstack(
            rx.button(
                
            ),
            rx.button(
                
            )
        )
    )


def dialog_form(
        trigger_button_config: dict,
        header_config: dict,
        # action_buttons_config: dict,
        form_to_use: rx.Component,
        on_submit: callable,
    ) -> rx.Component:
    
    return rx.dialog.root(
        trigger_button(
            **trigger_button_config
        ),
        rx.dialog.content(
            dialog_header(
                **header_config
            ),
            rx.flex(
                rx.form.root(
                    form_to_use(),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Submit Customer"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=on_submit,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
        )
    )