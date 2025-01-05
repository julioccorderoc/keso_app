# Header mapping

HEADER = "header"
TYPE = "type"
CONFIG = "config"
FILTER = "filter"
SORTABLE = "sortable"
HIDE = "hide"

header_mapping = {
    "cheese_batch_id": {
        HEADER: "cheese_batch_id",
        TYPE: "int",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: True
        }
    },
    "date": {
        HEADER: "Fecha",
        TYPE: "date",
        CONFIG: {
            FILTER: "date",
            SORTABLE: True,
            HIDE: False
        }
    },
    "user_id": {
        HEADER: "user_id",
        TYPE: "int",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: True
        }
    },
    "username": {
        HEADER: "Usuario",
        TYPE: "str",
        CONFIG: {
            FILTER: True,
            SORTABLE: False,
            HIDE: False
        }
    },
    "milk_used": {
        HEADER: "Leche usada",
        TYPE: "float",
        CONFIG: {
            FILTER: "number",
            SORTABLE: True,
            HIDE: False
        }
    },
    "salt_used": {
        HEADER: "Sal usada",
        TYPE: "float",
        CONFIG: {
            FILTER: "number",
            SORTABLE: True,
            HIDE: False
        }
    },
    "cheese": {
        HEADER: "Queso",
        TYPE: "float",
        CONFIG: {
            FILTER: "number",
            SORTABLE: True,
            HIDE: False
        }
    },
    "comments": {
        HEADER: "Comentarios",
        TYPE: "str",
        CONFIG: {
            FILTER: "text",
            SORTABLE: False,
            HIDE: False
        }
    },
    "cow_id": {
        HEADER: "cow_id",
        TYPE: "int",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: True
        }
    },
    "cow_code": {
        HEADER: "Vaca",
        TYPE: "str",
        CONFIG: {
            FILTER: True,
            SORTABLE: False,
            HIDE: False
        }
    },
    "cow_origin": {
        HEADER: "Origen",
        TYPE: "str",
        CONFIG: {
            FILTER: True,
            SORTABLE: False,
            HIDE: False
        }
    },
    "cow_age": {
        HEADER: "Edad",
        TYPE: "int",
        CONFIG: {
            FILTER: True,
            SORTABLE: True,
            HIDE: False
        }
    },
    "total_births": {
        HEADER: "Total de partos",
        TYPE: "int",
        CONFIG: {
            FILTER: True,
            SORTABLE: True,
            HIDE: False
        }
    },
    "total_milk": {
        HEADER: "Total de leche",
        TYPE: "float",
        CONFIG: {
            FILTER: "number",
            SORTABLE: True,
            HIDE: False
        }
    },
    "item_id": {
        HEADER: "item_id",
        TYPE: "int",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: True
        }
    },
    "item_name": {
        HEADER: "Item",
        TYPE: "str",
        CONFIG: {
            FILTER: True,
            SORTABLE: False,
            HIDE: False
        }
    },
    "quantity": {
        HEADER: "Cantidad",
        TYPE: "float",
        CONFIG: {
            FILTER: "number",
            SORTABLE: True,
            HIDE: False
        }
    },
    "measurement_unit": {
        HEADER: "Unidad",
        TYPE: "str",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: True
        }
    },
    "last_updated_date": {
        HEADER: "Actualizado el",
        TYPE: "date",
        CONFIG: {
            FILTER: "date",
            SORTABLE: True,
            HIDE: False
        }
    },
    "last_updated_by": {
        HEADER: "Actualizado por",
        TYPE: "str",
        CONFIG: {
            FILTER: True,
            SORTABLE: False,
            HIDE: False
        }
    },
    "milk_batch_id": {
        HEADER: "milk_batch_id",
        TYPE: "int",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: True
        }
    },
    "milk": {
        HEADER: "Leche",
        TYPE: "float",
        CONFIG: {
            FILTER: "number",
            SORTABLE: True,
            HIDE: False
        }
    },
    "system_log_id": {
        HEADER: "system_log_id",
        TYPE: "int",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: True
        }
    },
    "time": {
        HEADER: "Hora",
        TYPE: "time",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: False
        }
    },
    "action": {
        HEADER: "Acción",
        TYPE: "str",
        CONFIG: {
            FILTER: True,
            SORTABLE: False,
            HIDE: False
        }
    },
    "details": {
        HEADER: "Detalles",
        TYPE: "str",
        CONFIG: {
            FILTER: "text",
            SORTABLE: False,
            HIDE: False
        }
    },
    "transaction_id": {
        HEADER: "transaction_id",
        TYPE: "int",
        CONFIG: {
            FILTER: False,
            SORTABLE: False,
            HIDE: True
        }
    },
    "transaction_type": {
        HEADER: "Tipo de transacción",
        TYPE: "str",
        CONFIG: {
            FILTER: True,
            SORTABLE: False,
            HIDE: False
        }
    },
    "description": {
        HEADER: "Descripción",
        TYPE: "str",
        CONFIG: {
            FILTER: "text",
            SORTABLE: False,
            HIDE: False
        }
    },
    "amount": {
        HEADER: "Monto",
        TYPE: 'currency',
        CONFIG: {
            FILTER: "number",
            SORTABLE: True,
            HIDE: False
        }
    }
}