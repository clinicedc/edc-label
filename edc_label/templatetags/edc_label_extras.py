from django import template

register = template.Library()


@register.inclusion_tag("edc_label/print_button.html")
def print_button(button_label=None, printer=None, label_template_name=None, **kwargs):
    return dict(
        button_label=button_label,
        label_template_name=label_template_name,
        printer=printer,
    )


@register.inclusion_tag("edc_label/printer_config.html")
def printer_config(
    heading=None, printer_type=None, selected_printer=None, printers=None, **kwargs
):
    return dict(
        heading=heading,
        printer_type=printer_type,
        selected_printer=selected_printer,
        printers=printers,
    )
