--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: items; Type: TABLE; Schema: public; Owner: sur_user
--

CREATE TABLE public.items (
    id integer NOT NULL,
    name character varying,
    type character varying,
    weight double precision,
    size_x integer,
    size_y integer,
    player_id integer
);


ALTER TABLE public.items OWNER TO sur_user;

--
-- Name: items_id_seq; Type: SEQUENCE; Schema: public; Owner: sur_user
--

CREATE SEQUENCE public.items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.items_id_seq OWNER TO sur_user;

--
-- Name: items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sur_user
--

ALTER SEQUENCE public.items_id_seq OWNED BY public.items.id;


--
-- Name: players; Type: TABLE; Schema: public; Owner: sur_user
--

CREATE TABLE public.players (
    id integer NOT NULL,
    health integer,
    hunger integer,
    thirst integer,
    radiation integer
);


ALTER TABLE public.players OWNER TO sur_user;

--
-- Name: players_id_seq; Type: SEQUENCE; Schema: public; Owner: sur_user
--

CREATE SEQUENCE public.players_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.players_id_seq OWNER TO sur_user;

--
-- Name: players_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sur_user
--

ALTER SEQUENCE public.players_id_seq OWNED BY public.players.id;


--
-- Name: items id; Type: DEFAULT; Schema: public; Owner: sur_user
--

ALTER TABLE ONLY public.items ALTER COLUMN id SET DEFAULT nextval('public.items_id_seq'::regclass);


--
-- Name: players id; Type: DEFAULT; Schema: public; Owner: sur_user
--

ALTER TABLE ONLY public.players ALTER COLUMN id SET DEFAULT nextval('public.players_id_seq'::regclass);


--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: sur_user
--

COPY public.items (id, name, type, weight, size_x, size_y, player_id) FROM stdin;
1	Bandage	medical	0.5	1	1	1
2	Water	food	1	1	2	1
3	Berry	resource	1	1	1	1
4	Ration	resource	1	1	1	1
5	Berry	resource	1	1	1	1
6	Medkit	resource	1	1	1	1
\.


--
-- Data for Name: players; Type: TABLE DATA; Schema: public; Owner: sur_user
--

COPY public.players (id, health, hunger, thirst, radiation) FROM stdin;
1	80	100	100	0
\.


--
-- Name: items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sur_user
--

SELECT pg_catalog.setval('public.items_id_seq', 6, true);


--
-- Name: players_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sur_user
--

SELECT pg_catalog.setval('public.players_id_seq', 1, false);


--
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: sur_user
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: sur_user
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


--
-- Name: ix_items_id; Type: INDEX; Schema: public; Owner: sur_user
--

CREATE INDEX ix_items_id ON public.items USING btree (id);


--
-- Name: ix_players_id; Type: INDEX; Schema: public; Owner: sur_user
--

CREATE INDEX ix_players_id ON public.players USING btree (id);


--
-- Name: items items_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sur_user
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(id);


--
-- PostgreSQL database dump complete
--

