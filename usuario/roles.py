from rolepermissions.roles import AbstractUserRole

class Operador(AbstractUserRole):
    available_permissions = {
        'criar_ticket': True,
        'ver_ticket': True,
        'update_ticket': True,
    }

class Colaborador(AbstractUserRole):
    available_permissions = {
        'criar_ticket': True,
        'ver_ticket': True,
        'update_ticket': True,
    }

class Super(AbstractUserRole):
    available_permissions = {
        'ver_usuarios': True,
        'criar_ticket': True,
        'ver_ticket': True,
        'update_ticket': True,
    }