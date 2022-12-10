from vest import VestInfo
from chooser import *

vest23 = VestInfo(23)
# process
# Dacy - Diurno
vest23.vest23.skip(5)
vest23.modify_column(getTables(Quotas.TUDO), vest23.darcy["diurno"], "Cursos", vest23.get_sequence(), new_row=True )
# Darcy - Noturno
vest23.skip(1)
vest23.modify_column(getTables(Quotas.TUDO), vest23.darcy["noturno"], "Cursos", vest23.get_sequence(), new_row=True)
# Ceilandia - FCE
vest23.skip(2)
vest23.modify_column(getTables(Quotas.TUDO), vest23.fce, "Cursos", vest23.get_sequence(), new_row=True)
# Gama - FGA
vest23.skip(3)
vest23.modify_column(getTables(Quotas.TUDO), vest23.fga, "Cursos", vest23.get_sequence(), new_row=True)
# FUP - Diurno
vest23.skip(3)
vest23.modify_column(getTables(Quotas.TUDO), vest23.fup["diurno"], "Cursos", vest23.get_sequence(), new_row=True)
# FUP - Noturno
vest23.skip(1)
vest23.modify_column(getTables(Quotas.TUDO), vest23.fup["noturno"], "Cursos", vest23.get_sequence(), new_row=True)

# vest23.skipping column labels:
vest23.skip(122)

#
vest23.modify_column(getTables(Quotas.NEGROS), vest23.darcy["diurno"], "Vagas", vest23.get_sequence())
vest23.modify_column(getTables(Quotas.NEGROS), vest23.darcy["noturno"], "Vagas", vest23.get_sequence())
vest23.modify_column(getTables(Quotas.NEGROS), vest23.fce, "Vagas", vest23.get_sequence())
tmp = vest23.get_sequence()
tmp.extend(vest23.get_sequence())
vest23.modify_column(getTables(Quotas.NEGROS), vest23.fga, "Vagas", tmp)
vest23.modify_column(getTables(Quotas.NEGROS), vest23.fup["diurno"], "Vagas", vest23.get_sequence())
vest23.modify_column(getTables(Quotas.NEGROS), vest23.fup["diurno"], "Vagas", vest23.get_sequence())
vest23.modify_column(getTables(Quotas.NEGROS), vest23.fup["diurno"], "Vagas", vest23.get_sequence())
