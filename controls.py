PERIODS = []
years = [i for i in range(2008,2020)]
semesters = [1,2]
for year in years:
    for semester in semesters:
        if semester == 1 and year == 2008:
            continue
        if semester == 2 and year == 2019:
            continue
        else:
            PERIODS.append('{}_{}'.format(year,semester))

GEOGRAPHIC = dict(
    Department="Department",
    City="City"
    #School="School",
)

VARIABLES = {
    'ICFES Scores': {
        'PUNT_C_NATURALES',
        'PUNT_IDIOMA',
        'PUNT_LECTURA_CRITICA',
        'PUNT_MATEMATICAS',
        'PUNT_SOCIALES_CIUDADANAS',
        'PUNT_GLOBAL'
    },
    'Socioeconomic factors': {
        'ESTU_TRABAJA',
        'FAMI_DORMITORIOS_HOGAR',
        'FAMI_INGRESO_FMILIAR_MENSUAL',
        'FAMI_ESTRATO_VIVIENDA',
        'FAMI_NIVEL_SISBEN',
        'FAMI_PERSONAS_HOGAR',
        'FAMI_TELEFONO_FIJO',
        'FAMI_TIENEAUTOMOVIL',
        'FAMI_TIENECOMPUTADOR',
        'FAMI_TIENEINTERNET',
        'FAMI_TIENELAVADORA',
        'FAMI_TIENE_HORNO_MICROONDAS',
        'FAMI_TIENETELEVISOR',
        'FAMI_EDUCA_MADRE',
        'FAMI_EDUCA_PADRE',
        'FAMI_OCUPA_PADRE',
        'FAMI_OCUPA_MADRE',
        'ESTU_GENERO',
        'ESTU_JORNADA',
        'COLE_BILINGUE',
        'COLE_PAGA_PENSION',
        'COLE_NSE',
        'COLE_CALENDARIO_COLEGIO',
        'COLE_NATURALEZA'
    }
}


CATEGORICAL_VARIABLES = {
    'FAMI_EDUCA_MADRE': [
        'Ninguno', 
        'Postgrado',
        'Preescolar', 
        'Primaria',
        'Secundaria (Bachillerato)',
        'Titulo universitario',
        'Técnico o tecnológico' 
    ],
    'FAMI_EDUCA_PADRE': [
        'Ninguno', 
        'Postgrado',
        'Preescolar', 
        'Primaria',
        'Secundaria (Bachillerato)',
        'Titulo universitario',
        'Técnico o tecnológico' 
    ],
    'FAMI_OCUPA_PADRE': [
        'Empleado con cargo como director o gerente general',
        'Empleado de nivel auxiliar o administrativo',
        'Empleado de nivel directivo',
        'Empleado de nivel técnico o profesional',
        'Empleado obrero u operario',
        'Empresario', 
        'Hogar',
        'Otra actividad u ocupación',
        'Pensionado', 
        'Pequeño empresario',
        'Profesional Independiente',
        'Trabajador por cuenta propia'
    ],
    'FAMI_OCUPA_MADRE': [
        'Empleado con cargo como director o gerente general',
        'Empleado de nivel auxiliar o administrativo',
        'Empleado de nivel directivo',
        'Empleado de nivel técnico o profesional',
        'Empleado obrero u operario',
        'Empresario', 
        'Hogar',
        'Otra actividad u ocupación',
        'Pensionado', 
        'Pequeño empresario',
        'Profesional Independiente',
        'Trabajador por cuenta propia'
    ],
    'ESTU_GENERO': [
        'F', 
        'M' 
    ],
    'ESTU_JORNADA': [
        'COMPLETA',
        'MAÑANA', 
        'NOCHE',
        'SABATINA-DOMINICAL', 
        'TARDE',
        'UNICA' 
    ],
    'COLE_CALENDARIO_COLEGIO': [
        'A', 
        'B',
        'O'
    ],
    'COLE_NATURALEZA': [
        'NO OFICIAL',
        'OFICIAL'
    ]
}

WELL_COLORS = dict(
    GD="#FFEDA0",
    GE="#FA9FB5",
    GW="#A1D99B",
    IG="#67BD65",
    OD="#BFD3E6",
    OE="#B3DE69",
    OW="#FDBF6F",
    ST="#FC9272",
    BR="#D0D1E6",
    MB="#ABD9E9",
    IW="#3690C0",
    LP="#F87A72",
    MS="#CA6BCC",
    Confidential="#DD3497",
    DH="#4EB3D3",
    DS="#FFFF33",
    DW="#FB9A99",
    MM="#A6D853",
    NL="#D4B9DA",
    OB="#AEB0B8",
    SG="#CCCCCC",
    TH="#EAE5D9",
    UN="#C29A84",
)

DEPARTAMENTOS = ['BOGOTA', 'SANTANDER', 'MAGDALENA', 'RISARALDA', 'CASANARE',
       'ATLANTICO', 'LA GUAJIRA', 'ANTIOQUIA', 'BOYACA', 'CESAR',
       'PUTUMAYO', 'SUCRE', 'NORTE SANTANDER', 'VICHADA', 'GUAVIARE',
       'BOLIVAR', 'CALDAS', 'QUINDIO', 'CUNDINAMARCA', 'SAN ANDRES',
       'META', 'CORDOBA', 'CHOCO', 'ARAUCA', 'TOLIMA', 'AMAZONAS',
       'CAUCA', 'HUILA', 'CAQUETA', 'VALLE', 'NARIÑO', 'VAUPES',
       'GUAINIA']

PUNTAJES = ['PUNT_GLOBAL', 'PUNT_C_NATURALES', 'PUNT_IDIOMA',
            'PUNT_LECTURA_CRITICA', 'PUNT_MATEMATICAS', 'PUNT_SOCIALES_CIUDADANAS']


VARIABLES_DETAILED_DASHBOARD = [
    'COLE_CATEGORIA',
    'COLE_GENEROPOBLACION', 
    'COLE_NATURALEZA', 
    'COLE_AREA_UBICACION', 
    'COLE_BILINGUE', 
    'COLE_CARACTER', 
    'COLE_PAGA_PENSION', 
    'COLE_NSE'
]

VariablesACambiar=[
    'ESTU_TRABAJA',
    'FAMI_TIENECOMPUTADOR',
    'COBERTURA_NETA'
]