% DEPORTES

deporte(futbol).
deporte(basquetbol).
deporte(voleibol).
deporte(natacion).
deporte(tenis).

% MODALIDADES

modalidad(futbol, futbol_11).
modalidad(futbol, futsal).
modalidad(futbol, futbol_rapido).

modalidad(basquetbol, basquetbol_3x3).
modalidad(basquetbol, basquetbol_silla_ruedas).
modalidad(basquetbol, basquetbol_profesional).

modalidad(voleibol, voleibol_playa).
modalidad(voleibol, voleibol_sentado).
modalidad(voleibol, voleibol_sala).

modalidad(natacion, natacion_velocidad).
modalidad(natacion, natacion_aguas_abiertas).
modalidad(natacion, natacion_artistica).

modalidad(tenis, tenis_individual).
modalidad(tenis, tenis_parejas).
modalidad(tenis, tenis_silla_ruedas).

% JUGADORES POR EQUIPO

jugadores(futbol_11, 11).
jugadores(futsal, 5).
jugadores(futbol_rapido, 7).

jugadores(basquetbol_3x3, 3).
jugadores(basquetbol_silla_ruedas, 5).
jugadores(basquetbol_profesional, 5).

jugadores(voleibol_playa, 2).
jugadores(voleibol_sentado, 6).
jugadores(voleibol_sala, 6).

jugadores(natacion_velocidad, 1).
jugadores(natacion_aguas_abiertas, 1).
jugadores(natacion_artistica, 1).

jugadores(tenis_individual, 1).
jugadores(tenis_parejas, 2).
jugadores(tenis_silla_ruedas, 1).

% INTENSIDAD FISICA

intensidad(futbol_11, media).
intensidad(futsal, alta).
intensidad(futbol_rapido, alta).

intensidad(basquetbol_3x3, alta).
intensidad(basquetbol_silla_ruedas, alta).
intensidad(basquetbol_profesional, alta).

intensidad(voleibol_playa, media).
intensidad(voleibol_sentado, baja).
intensidad(voleibol_sala, media).

intensidad(natacion_velocidad, alta).
intensidad(natacion_aguas_abiertas, alta).
intensidad(natacion_artistica, media).

intensidad(tenis_individual, alta).
intensidad(tenis_parejas, media).
intensidad(tenis_silla_ruedas, media).

% LUGAR DONDE SE PRACTICA

lugar(futbol_11, exterior).
lugar(futsal, interior).
lugar(futbol_rapido, exterior).

lugar(basquetbol_3x3, exterior).
lugar(basquetbol_silla_ruedas, interior).
lugar(basquetbol_profesional, interior).

lugar(voleibol_playa, exterior).
lugar(voleibol_sentado, interior).
lugar(voleibol_sala, interior).

lugar(natacion_velocidad, agua).
lugar(natacion_aguas_abiertas, agua).
lugar(natacion_artistica, agua).

lugar(tenis_individual, exterior).
lugar(tenis_parejas, exterior).
lugar(tenis_silla_ruedas, exterior).

% REGLAS DE CONSULTA

modalidades_de(Deporte, Modalidad) :-
    modalidad(Deporte, Modalidad).

obtener_jugadores(Modalidad, Jugadores) :-
    jugadores(Modalidad, Jugadores).

obtener_intensidad(Modalidad, Intensidad) :-
    intensidad(Modalidad, Intensidad).

modalidades_por_lugar(Lugar, Modalidad) :-
    lugar(Modalidad, Lugar).

% SISTEMA DE RECOMENDACION

% Recomienda modalidades segun la intensidad que la persona quiere y el lugar
recomendar_modalidad(Intensidad, Lugar, Modalidad) :-
    intensidad(Modalidad, Intensidad),
    lugar(Modalidad, Lugar).