import reflex as rx
from ...states import Dialogs_State


def _dialog_header(
        icon: str,
        title: str,
        description: str, 
    ) -> rx.Component:
    
    return rx.box(
        rx.hstack(
            rx.badge(
                rx.icon(tag=icon, size=34),
                radius="full",
                padding="0.65rem",
                ),
            rx.vstack(
                rx.dialog.title(
                    title,
                    weight="bold",
                    margin="0",
                ),
                rx.dialog.description(description),
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
    
    
def _action_buttons(
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


def _dialog_actions(
        dialog_to_open: str,
        resubmit_form: bool,
        primary_button_text: str,
        secondary_button_text: str,
    ) -> rx.Component:
    
    return rx.flex(
        rx.dialog.close(
            rx.button(
                secondary_button_text,
                variant="soft",
                color_scheme="gray",
                on_click=Dialogs_State.setvar(dialog_to_open, False),
            ),
        ),
        rx.form.submit(
            rx.dialog.close(
                rx.button(
                    primary_button_text,
                    on_click=Dialogs_State.setvar(dialog_to_open, resubmit_form)
                ),
            ),
            as_child=True,
        ),
        padding_top="2em",
        spacing="3",
        mt="4",
        justify="end",
    )





def dialog_form(
        header: dict,
        form_to_use: rx.Component,
        on_submit: callable,
        dialog_to_open: str,
        resubmit_form: bool,
        primary_button_text: str,
        secondary_button_text: str = "Listo",
    ) -> rx.Component:
    
    return rx.dialog.root(
        rx.dialog.content(
            _dialog_header(
                **header
            ),
            rx.flex(
                rx.form.root(
                    form_to_use(),
                    _dialog_actions(
                        dialog_to_open,
                        resubmit_form,
                        primary_button_text,
                        secondary_button_text
                    ),
                    on_submit=on_submit,
                    reset_on_submit=resubmit_form,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            on_pointer_down_outside=Dialogs_State.setvar(dialog_to_open, False),
            on_escape_key_down=Dialogs_State.setvar(dialog_to_open, False)
        ),
        open=getattr(Dialogs_State, dialog_to_open),
        on_open_change=lambda state_change: Dialogs_State.setvar(dialog_to_open, state_change)
    )