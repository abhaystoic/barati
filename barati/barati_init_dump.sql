--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: insert_new_user_in_users(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION insert_new_user_in_users() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
   INSERT INTO users(username, first_name, last_name, email, role) VALUES(NEW.username, NEW.first_name, NEW.last_name, NEW.email, 'vendor');
   RETURN NEW;
END;
$$;


ALTER FUNCTION public.insert_new_user_in_users() OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: address; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE address (
    id integer NOT NULL,
    building_number character varying(50),
    street character varying(100),
    locality character varying(50),
    landmark character varying(50),
    city character varying(50),
    state character varying(50),
    country character varying(50),
    zipcode character varying(50),
    "timestamp" timestamp with time zone,
    type character varying(10) NOT NULL
);


ALTER TABLE address OWNER TO postgres;

--
-- Name: address_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE address_id_seq OWNER TO postgres;

--
-- Name: address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE address_id_seq OWNED BY address.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: axes_accessattempt; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE axes_accessattempt (
    id integer NOT NULL,
    user_agent character varying(255) NOT NULL,
    ip_address inet,
    username character varying(255),
    trusted boolean NOT NULL,
    http_accept character varying(1025) NOT NULL,
    path_info character varying(255) NOT NULL,
    attempt_time timestamp with time zone NOT NULL,
    get_data text NOT NULL,
    post_data text NOT NULL,
    failures_since_start integer NOT NULL,
    CONSTRAINT axes_accessattempt_failures_since_start_check CHECK ((failures_since_start >= 0))
);


ALTER TABLE axes_accessattempt OWNER TO postgres;

--
-- Name: axes_accessattempt_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE axes_accessattempt_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE axes_accessattempt_id_seq OWNER TO postgres;

--
-- Name: axes_accessattempt_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE axes_accessattempt_id_seq OWNED BY axes_accessattempt.id;


--
-- Name: axes_accesslog; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE axes_accesslog (
    id integer NOT NULL,
    user_agent character varying(255) NOT NULL,
    ip_address inet,
    username character varying(255),
    trusted boolean NOT NULL,
    http_accept character varying(1025) NOT NULL,
    path_info character varying(255) NOT NULL,
    attempt_time timestamp with time zone NOT NULL,
    logout_time timestamp with time zone
);


ALTER TABLE axes_accesslog OWNER TO postgres;

--
-- Name: axes_accesslog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE axes_accesslog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE axes_accesslog_id_seq OWNER TO postgres;

--
-- Name: axes_accesslog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE axes_accesslog_id_seq OWNED BY axes_accesslog.id;


--
-- Name: bakery_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE bakery_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE bakery_types OWNER TO postgres;

--
-- Name: bakery_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE bakery_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bakery_types_id_seq OWNER TO postgres;

--
-- Name: bakery_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE bakery_types_id_seq OWNED BY bakery_types.id;


--
-- Name: band_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE band_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE band_types OWNER TO postgres;

--
-- Name: band_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE band_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE band_types_id_seq OWNER TO postgres;

--
-- Name: band_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE band_types_id_seq OWNED BY band_types.id;


--
-- Name: beautician_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE beautician_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE beautician_types OWNER TO postgres;

--
-- Name: beautician_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE beautician_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE beautician_types_id_seq OWNER TO postgres;

--
-- Name: beautician_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE beautician_types_id_seq OWNED BY beautician_types.id;


--
-- Name: beauticians; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE beauticians (
    id integer NOT NULL,
    ref_id character varying(100) NOT NULL,
    name character varying(100) NOT NULL,
    short_description character varying(100),
    long_description character varying(800),
    services character varying(800),
    actual_price double precision NOT NULL,
    discount_rs double precision,
    discounted_price double precision,
    female_person_available boolean,
    home_visit_charge double precision,
    type_id integer,
    vendor_id integer NOT NULL,
    gender character varying(10) NOT NULL,
    home_visit_policy character varying(800),
    barati_confidence_perc double precision,
    "timestamp" timestamp with time zone,
    discount_perc double precision,
    address_id integer
);


ALTER TABLE beauticians OWNER TO postgres;

--
-- Name: beauticians_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE beauticians_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE beauticians_id_seq OWNER TO postgres;

--
-- Name: beauticians_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE beauticians_id_seq OWNED BY beauticians.id;


--
-- Name: budget; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE budget (
    id integer NOT NULL,
    min_master double precision,
    max_master double precision,
    min_venue double precision,
    max_venue double precision,
    min_card double precision,
    max_card double precision,
    min_beautician double precision,
    max_beautician double precision,
    min_mehendi double precision,
    max_mehendi double precision,
    min_music double precision,
    max_music double precision,
    min_gift double precision,
    max_gift double precision,
    min_tent double precision,
    max_tent double precision,
    user_id integer NOT NULL
);


ALTER TABLE budget OWNER TO postgres;

--
-- Name: budget_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE budget_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE budget_id_seq OWNER TO postgres;

--
-- Name: budget_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE budget_id_seq OWNED BY budget.id;


--
-- Name: card_colors; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE card_colors (
    id integer NOT NULL,
    ref_id character varying(100),
    color character varying(20),
    hexcode character varying(7),
    card_id integer
);


ALTER TABLE card_colors OWNER TO postgres;

--
-- Name: card_colors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE card_colors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE card_colors_id_seq OWNER TO postgres;

--
-- Name: card_colors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE card_colors_id_seq OWNED BY card_colors.id;


--
-- Name: card_deities; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE card_deities (
    id integer NOT NULL,
    ref_id character varying(100),
    top_deity_name character varying(30),
    inner_deity_name character varying(30),
    card_id integer,
    inner_deity_image_path character varying(200),
    top_deity_image_path character varying(200)
);


ALTER TABLE card_deities OWNER TO postgres;

--
-- Name: card_deities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE card_deities_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE card_deities_id_seq OWNER TO postgres;

--
-- Name: card_deities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE card_deities_id_seq OWNED BY card_deities.id;


--
-- Name: card_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE card_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE card_types OWNER TO postgres;

--
-- Name: card_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE card_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE card_types_id_seq OWNER TO postgres;

--
-- Name: card_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE card_types_id_seq OWNED BY card_types.id;


--
-- Name: cards; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE cards (
    id integer NOT NULL,
    ref_id character varying(100) NOT NULL,
    name character varying(100) NOT NULL,
    short_description character varying(100) NOT NULL,
    long_description character varying(800) NOT NULL,
    min_numbers integer NOT NULL,
    max_numbers integer NOT NULL,
    type_id integer,
    vendor_id integer NOT NULL,
    actual_price double precision NOT NULL,
    discount_rs double precision,
    discounted_price double precision,
    length double precision,
    width double precision,
    weight double precision,
    printing_price double precision,
    barati_confidence_perc double precision,
    "timestamp" timestamp with time zone,
    discount_perc double precision,
    address_id integer
);


ALTER TABLE cards OWNER TO postgres;

--
-- Name: cards_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE cards_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cards_id_seq OWNER TO postgres;

--
-- Name: cards_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE cards_id_seq OWNED BY cards.id;


--
-- Name: cards_preferences; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE cards_preferences (
    id integer NOT NULL,
    ref_id character varying(100) NOT NULL,
    avail_printing boolean,
    card_id integer NOT NULL,
    user_id integer
);


ALTER TABLE cards_preferences OWNER TO postgres;

--
-- Name: cards_preferences_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE cards_preferences_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cards_preferences_id_seq OWNER TO postgres;

--
-- Name: cards_preferences_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE cards_preferences_id_seq OWNED BY cards_preferences.id;


--
-- Name: cart; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE cart (
    id integer NOT NULL,
    ref_id character varying(100) NOT NULL,
    product_type character varying(50) NOT NULL,
    checked_out boolean NOT NULL,
    quantity integer,
    user_id integer NOT NULL,
    total_price double precision
);


ALTER TABLE cart OWNER TO postgres;

--
-- Name: cart_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE cart_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cart_id_seq OWNER TO postgres;

--
-- Name: cart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE cart_id_seq OWNED BY cart.id;


--
-- Name: delivery_status; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE delivery_status (
    id integer NOT NULL,
    ref_id character varying(100),
    name character varying(100),
    status character varying(100),
    link character varying(200),
    "timestamp" timestamp with time zone NOT NULL,
    order_id integer
);


ALTER TABLE delivery_status OWNER TO postgres;

--
-- Name: delivery_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE delivery_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE delivery_status_id_seq OWNER TO postgres;

--
-- Name: delivery_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE delivery_status_id_seq OWNED BY delivery_status.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO postgres;

--
-- Name: fireworks_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE fireworks_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE fireworks_types OWNER TO postgres;

--
-- Name: fireworks_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE fireworks_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE fireworks_types_id_seq OWNER TO postgres;

--
-- Name: fireworks_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE fireworks_types_id_seq OWNED BY fireworks_types.id;


--
-- Name: ghodi_bagghi_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ghodi_bagghi_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE ghodi_bagghi_types OWNER TO postgres;

--
-- Name: ghodi_bagghi_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ghodi_bagghi_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ghodi_bagghi_types_id_seq OWNER TO postgres;

--
-- Name: ghodi_bagghi_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ghodi_bagghi_types_id_seq OWNED BY ghodi_bagghi_types.id;


--
-- Name: gift_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE gift_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE gift_types OWNER TO postgres;

--
-- Name: gift_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE gift_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE gift_types_id_seq OWNER TO postgres;

--
-- Name: gift_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE gift_types_id_seq OWNED BY gift_types.id;


--
-- Name: main_preferences; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE main_preferences (
    id integer NOT NULL,
    date date,
    location character varying(50),
    sublocation character varying(50),
    user_id integer NOT NULL
);


ALTER TABLE main_preferences OWNER TO postgres;

--
-- Name: main_preferences_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE main_preferences_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE main_preferences_id_seq OWNER TO postgres;

--
-- Name: main_preferences_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE main_preferences_id_seq OWNED BY main_preferences.id;


--
-- Name: mehendi_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE mehendi_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE mehendi_types OWNER TO postgres;

--
-- Name: mehendi_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE mehendi_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mehendi_types_id_seq OWNER TO postgres;

--
-- Name: mehendi_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE mehendi_types_id_seq OWNED BY mehendi_types.id;


--
-- Name: music_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE music_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE music_types OWNER TO postgres;

--
-- Name: music_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE music_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE music_types_id_seq OWNER TO postgres;

--
-- Name: music_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE music_types_id_seq OWNED BY music_types.id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE orders (
    order_id integer NOT NULL,
    ref_id character varying(100) NOT NULL,
    quantity integer,
    total_price double precision,
    package_id character varying(100) NOT NULL,
    vendor_acknowledgement character varying(51) NOT NULL,
    payment_done boolean NOT NULL,
    payment_received boolean NOT NULL,
    payment_method character varying(100),
    product_type character varying(100),
    "timestamp" timestamp with time zone NOT NULL,
    address_id integer,
    user_id integer,
    vendor_id integer,
    comment character varying(500),
    last_status_time timestamp with time zone
);


ALTER TABLE orders OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE orders_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE orders_id_seq OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE orders_id_seq OWNED BY orders.order_id;


--
-- Name: photo_video_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE photo_video_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE photo_video_types OWNER TO postgres;

--
-- Name: product_pictures; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE product_pictures (
    id integer NOT NULL,
    name character varying(100),
    ref_id character varying(100),
    picture_path character varying(200),
    picture character varying(100)
);


ALTER TABLE product_pictures OWNER TO postgres;

--
-- Name: product_pictures_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE product_pictures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE product_pictures_id_seq OWNER TO postgres;

--
-- Name: product_pictures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE product_pictures_id_seq OWNED BY product_pictures.id;


--
-- Name: religion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE religion (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE religion OWNER TO postgres;

--
-- Name: religion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE religion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE religion_id_seq OWNER TO postgres;

--
-- Name: religion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE religion_id_seq OWNED BY religion.id;


--
-- Name: reviews; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE reviews (
    id integer NOT NULL,
    ref_id character varying(100),
    "timestamp" timestamp with time zone NOT NULL,
    title character varying(200),
    detailed_review character varying(1000),
    recommended character varying(10),
    user_id integer
);


ALTER TABLE reviews OWNER TO postgres;

--
-- Name: reviews_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE reviews_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE reviews_id_seq OWNER TO postgres;

--
-- Name: reviews_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE reviews_id_seq OWNED BY reviews.id;


--
-- Name: social_auth_association; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE social_auth_association (
    id integer NOT NULL,
    server_url character varying(255) NOT NULL,
    handle character varying(255) NOT NULL,
    secret character varying(255) NOT NULL,
    issued integer NOT NULL,
    lifetime integer NOT NULL,
    assoc_type character varying(64) NOT NULL
);


ALTER TABLE social_auth_association OWNER TO postgres;

--
-- Name: social_auth_association_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE social_auth_association_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_association_id_seq OWNER TO postgres;

--
-- Name: social_auth_association_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE social_auth_association_id_seq OWNED BY social_auth_association.id;


--
-- Name: social_auth_code; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE social_auth_code (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    code character varying(32) NOT NULL,
    verified boolean NOT NULL
);


ALTER TABLE social_auth_code OWNER TO postgres;

--
-- Name: social_auth_code_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE social_auth_code_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_code_id_seq OWNER TO postgres;

--
-- Name: social_auth_code_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE social_auth_code_id_seq OWNED BY social_auth_code.id;


--
-- Name: social_auth_nonce; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE social_auth_nonce (
    id integer NOT NULL,
    server_url character varying(255) NOT NULL,
    "timestamp" integer NOT NULL,
    salt character varying(65) NOT NULL
);


ALTER TABLE social_auth_nonce OWNER TO postgres;

--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE social_auth_nonce_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_nonce_id_seq OWNER TO postgres;

--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE social_auth_nonce_id_seq OWNED BY social_auth_nonce.id;


--
-- Name: social_auth_usersocialauth; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE social_auth_usersocialauth (
    id integer NOT NULL,
    provider character varying(32) NOT NULL,
    uid character varying(255) NOT NULL,
    extra_data text NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE social_auth_usersocialauth OWNER TO postgres;

--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE social_auth_usersocialauth_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE social_auth_usersocialauth_id_seq OWNER TO postgres;

--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE social_auth_usersocialauth_id_seq OWNED BY social_auth_usersocialauth.id;


--
-- Name: star_ratings_rating; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE star_ratings_rating (
    id integer NOT NULL,
    count integer NOT NULL,
    total integer NOT NULL,
    average numeric(6,3) NOT NULL,
    object_id integer,
    content_type_id integer,
    CONSTRAINT star_ratings_rating_count_check CHECK ((count >= 0)),
    CONSTRAINT star_ratings_rating_object_id_check CHECK ((object_id >= 0)),
    CONSTRAINT star_ratings_rating_total_check CHECK ((total >= 0))
);


ALTER TABLE star_ratings_rating OWNER TO postgres;

--
-- Name: star_ratings_rating_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE star_ratings_rating_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE star_ratings_rating_id_seq OWNER TO postgres;

--
-- Name: star_ratings_rating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE star_ratings_rating_id_seq OWNED BY star_ratings_rating.id;


--
-- Name: star_ratings_userrating; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE star_ratings_userrating (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    ip inet,
    score smallint NOT NULL,
    rating_id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT star_ratings_userrating_score_check CHECK ((score >= 0))
);


ALTER TABLE star_ratings_userrating OWNER TO postgres;

--
-- Name: star_ratings_userrating_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE star_ratings_userrating_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE star_ratings_userrating_id_seq OWNER TO postgres;

--
-- Name: star_ratings_userrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE star_ratings_userrating_id_seq OWNED BY star_ratings_userrating.id;


--
-- Name: tax_and_refund_policies; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tax_and_refund_policies (
    id integer NOT NULL,
    product_type character varying(100),
    total_tax double precision,
    min_payment_needed_before_confirmation double precision,
    refund_before_confirmation double precision,
    refund_after_30_days_or_processing double precision,
    refund_after_die_preparing double precision,
    refund_between_15_30_days double precision,
    "timestamp" timestamp with time zone,
    refund_between_2_7_days double precision,
    refund_between_7_15_days double precision,
    refund_within_2_days double precision
);


ALTER TABLE tax_and_refund_policies OWNER TO postgres;

--
-- Name: tax_and_refund_policies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tax_and_refund_policies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tax_and_refund_policies_id_seq OWNER TO postgres;

--
-- Name: tax_and_refund_policies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tax_and_refund_policies_id_seq OWNED BY tax_and_refund_policies.id;


--
-- Name: tent_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tent_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE tent_types OWNER TO postgres;

--
-- Name: tent_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tent_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tent_types_id_seq OWNER TO postgres;

--
-- Name: tent_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tent_types_id_seq OWNED BY tent_types.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE users (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    first_name character varying(50),
    middle_name character varying(100),
    last_name character varying(50),
    email character varying(100),
    contact1 character varying(50),
    contact2 character varying(50),
    contact3 character varying(50),
    address_id integer,
    religion_id integer,
    role character varying(10) NOT NULL
);


ALTER TABLE users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE users_id_seq OWNED BY users.id;


--
-- Name: vendor_coordinators; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vendor_coordinators (
    id integer NOT NULL,
    coordinator_name character varying(100) NOT NULL,
    email character varying(100),
    contact1 character varying(50) NOT NULL,
    contact2 character varying(50) NOT NULL,
    contact3 character varying(50) NOT NULL,
    vendor_id integer
);


ALTER TABLE vendor_coordinators OWNER TO postgres;

--
-- Name: vendor_coordinators_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE vendor_coordinators_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE vendor_coordinators_id_seq OWNER TO postgres;

--
-- Name: vendor_coordinators_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE vendor_coordinators_id_seq OWNED BY vendor_coordinators.id;


--
-- Name: vendors; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vendors (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    official_email character varying(100),
    contact1 character varying(50),
    contact2 character varying(50),
    contact3 character varying(50),
    address_id integer,
    user_id integer NOT NULL
);


ALTER TABLE vendors OWNER TO postgres;

--
-- Name: vendors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE vendors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE vendors_id_seq OWNER TO postgres;

--
-- Name: vendors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE vendors_id_seq OWNED BY vendors.id;


--
-- Name: venue_types; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE venue_types (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE venue_types OWNER TO postgres;

--
-- Name: venue_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE venue_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE venue_types_id_seq OWNER TO postgres;

--
-- Name: venue_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE venue_types_id_seq OWNED BY venue_types.id;


--
-- Name: venues; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE venues (
    id integer NOT NULL,
    ref_id character varying(100) NOT NULL,
    name character varying(100) NOT NULL,
    short_description character varying(100) NOT NULL,
    long_description character varying(800) NOT NULL,
    max_capacity integer NOT NULL,
    accomodation_available boolean NOT NULL,
    address_id integer,
    type_id integer,
    vendor_id integer NOT NULL,
    actual_price double precision NOT NULL,
    discount_perc double precision,
    discount_rs double precision,
    discounted_price double precision,
    "timestamp" timestamp with time zone,
    audio_video_equipment_details character varying(800),
    cutlery_and_crockery_details character varying(800),
    food_types character varying(800),
    function_types character varying(800),
    generator_details character varying(800),
    rooms_details character varying(800),
    number_of_rooms integer,
    outside_catering_allowed boolean,
    outside_decoration_allowed boolean,
    generator_cost double precision,
    per_plate_cost_nonveg double precision,
    per_plate_cost_veg double precision,
    per_room_per_day_cost double precision,
    service_staff_details character varying(800),
    stage_details character varying(800),
    valet_parking boolean,
    generator_available boolean,
    generator_cost_type character varying(50),
    parking_capacity_2_wheelers integer,
    parking_capacity_4_wheelers integer,
    wheelchair_accessibility character varying(50),
    alcohol_serving boolean
);


ALTER TABLE venues OWNER TO postgres;

--
-- Name: venues_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE venues_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE venues_id_seq OWNER TO postgres;

--
-- Name: venues_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE venues_id_seq OWNED BY venues.id;


--
-- Name: video_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE video_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE video_types_id_seq OWNER TO postgres;

--
-- Name: video_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE video_types_id_seq OWNED BY photo_video_types.id;


--
-- Name: videos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE videos (
    id integer NOT NULL,
    ref_id character varying(100) NOT NULL,
    video_name character varying(50) NOT NULL,
    video_link character varying(100) NOT NULL,
    vendor_id_id integer
);


ALTER TABLE videos OWNER TO postgres;

--
-- Name: videos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE videos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE videos_id_seq OWNER TO postgres;

--
-- Name: videos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE videos_id_seq OWNED BY videos.id;


--
-- Name: wishlist; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE wishlist (
    id integer NOT NULL,
    ref_id character varying(100),
    "timestamp" timestamp with time zone NOT NULL,
    user_id integer
);


ALTER TABLE wishlist OWNER TO postgres;

--
-- Name: wishlist_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE wishlist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE wishlist_id_seq OWNER TO postgres;

--
-- Name: wishlist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE wishlist_id_seq OWNED BY wishlist.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY address ALTER COLUMN id SET DEFAULT nextval('address_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY axes_accessattempt ALTER COLUMN id SET DEFAULT nextval('axes_accessattempt_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY axes_accesslog ALTER COLUMN id SET DEFAULT nextval('axes_accesslog_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY bakery_types ALTER COLUMN id SET DEFAULT nextval('bakery_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY band_types ALTER COLUMN id SET DEFAULT nextval('band_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY beautician_types ALTER COLUMN id SET DEFAULT nextval('beautician_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY beauticians ALTER COLUMN id SET DEFAULT nextval('beauticians_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY budget ALTER COLUMN id SET DEFAULT nextval('budget_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY card_colors ALTER COLUMN id SET DEFAULT nextval('card_colors_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY card_deities ALTER COLUMN id SET DEFAULT nextval('card_deities_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY card_types ALTER COLUMN id SET DEFAULT nextval('card_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cards ALTER COLUMN id SET DEFAULT nextval('cards_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cards_preferences ALTER COLUMN id SET DEFAULT nextval('cards_preferences_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cart ALTER COLUMN id SET DEFAULT nextval('cart_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY delivery_status ALTER COLUMN id SET DEFAULT nextval('delivery_status_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY fireworks_types ALTER COLUMN id SET DEFAULT nextval('fireworks_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ghodi_bagghi_types ALTER COLUMN id SET DEFAULT nextval('ghodi_bagghi_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY gift_types ALTER COLUMN id SET DEFAULT nextval('gift_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY main_preferences ALTER COLUMN id SET DEFAULT nextval('main_preferences_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mehendi_types ALTER COLUMN id SET DEFAULT nextval('mehendi_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY music_types ALTER COLUMN id SET DEFAULT nextval('music_types_id_seq'::regclass);


--
-- Name: order_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY orders ALTER COLUMN order_id SET DEFAULT nextval('orders_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY photo_video_types ALTER COLUMN id SET DEFAULT nextval('video_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY product_pictures ALTER COLUMN id SET DEFAULT nextval('product_pictures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY religion ALTER COLUMN id SET DEFAULT nextval('religion_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reviews ALTER COLUMN id SET DEFAULT nextval('reviews_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY social_auth_association ALTER COLUMN id SET DEFAULT nextval('social_auth_association_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY social_auth_code ALTER COLUMN id SET DEFAULT nextval('social_auth_code_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY social_auth_nonce ALTER COLUMN id SET DEFAULT nextval('social_auth_nonce_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY social_auth_usersocialauth ALTER COLUMN id SET DEFAULT nextval('social_auth_usersocialauth_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY star_ratings_rating ALTER COLUMN id SET DEFAULT nextval('star_ratings_rating_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY star_ratings_userrating ALTER COLUMN id SET DEFAULT nextval('star_ratings_userrating_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tax_and_refund_policies ALTER COLUMN id SET DEFAULT nextval('tax_and_refund_policies_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tent_types ALTER COLUMN id SET DEFAULT nextval('tent_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vendor_coordinators ALTER COLUMN id SET DEFAULT nextval('vendor_coordinators_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vendors ALTER COLUMN id SET DEFAULT nextval('vendors_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY venue_types ALTER COLUMN id SET DEFAULT nextval('venue_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY venues ALTER COLUMN id SET DEFAULT nextval('venues_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY videos ALTER COLUMN id SET DEFAULT nextval('videos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY wishlist ALTER COLUMN id SET DEFAULT nextval('wishlist_id_seq'::regclass);


--
-- Data for Name: address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY address (id, building_number, street, locality, landmark, city, state, country, zipcode, "timestamp", type) FROM stdin;
1	21	\N	Chawari Bazar	\N	Delhi	Delhi	India	10006	2016-01-01 21:56:57.799018+05:30	vendor
2			Chhatarpur		New Delhi	Delhi	India		2016-01-01 21:56:57.799018+05:30	vendor
3	12	JL Road	Chandani Chawk	Near Hanuman Mandir	Delhi	Delhi	India	11001	2016-01-21 17:22:50.554278+05:30	delivery
5	10	test street	test locality	test landmark	Delhi	Delhi	India	100001	2016-02-01 23:08:24.180714+05:30	
17	11	test street	test locality	test landmark	Delhi	Delhi	India	100002	2016-02-02 00:25:45.950853+05:30	
18	12	test street	test locality	test landmark	Delhi	Delhi	India	100001	2016-02-02 01:01:37.942622+05:30	
19	121	test street	Chandani Chauk	Near metro station	Old Delhi	Delhi	India	100006	2016-02-03 11:28:43.636676+05:30	
20	121	test street	Chandani Chauk	Near metro station	Old Delhi	Delhi	India	100006	2016-02-03 11:31:53.669273+05:30	
21	121	test street	Chandani Chauk	Near metro station	Old Delhi	Delhi	India	100006	2016-02-03 11:33:05.826268+05:30	
22	121	test street	Chandani Chauk	Near metro station	Old Delhi	Delhi	India	100006	2016-02-03 11:36:27.988547+05:30	
23	121	test street	Chandani Chauk	Near metro station	Old Delhi	\N	\N	100006	2016-02-03 11:53:06.467881+05:30	
24	121	test street	Chandani Chauk	Near metro station	Old Delhi	\N	\N	100006	2016-02-03 11:53:28.961565+05:30	
26	\N	\N	Chandani Chauk	\N	\N	\N	\N	100006	2016-02-03 11:55:22.183043+05:30	
27	\N	\N	Chandani Chauk	\N	\N	\N	\N	100006	2016-02-03 11:55:37.509928+05:30	
28	\N	\N	Chandani Chauk	\N	\N	\N	\N	100006	2016-02-03 11:55:42.10822+05:30	
29	\N	\N	Chandani Chauk	\N	\N	\N	\N	100006	2016-02-03 11:56:29.752609+05:30	
30	\N	\N	Chandani Chauk	\N	\N	\N	\N	100006	2016-02-03 11:56:48.476051+05:30	
32	\N	\N	Chandani Chauk	Near metro station	\N	\N	\N	100006	2016-02-03 11:58:34.291607+05:30	
33	\N	\N	Chandani Chauk	Near metro station	\N	\N	\N	100006	2016-02-03 11:59:02.89651+05:30	
34	\N	\N	Chandani Chauk	Near metro station	\N	\N	\N	100006	2016-02-03 11:59:51.373639+05:30	
35	\N	\N	Chandani Chauk	\N	\N	\N	\N	100006	2016-02-03 12:06:17.856539+05:30	
36	121	test street	Chandani Chauk	Near metro station	Old Delhi	Delhi	India	100006	2016-02-03 12:10:58.624191+05:30	
37	\N	\N	Chandani Chauk	\N	Delhi	\N	\N	100006	2016-02-03 12:20:49.635448+05:30	
38	\N	\N	Chandani Chauk	\N	Delhi	\N	\N	100006	2016-02-03 12:22:14.340767+05:30	
39	\N	\N	Chandani Chauk	\N	Delhi	\N	\N	100006	2016-02-03 12:22:37.009893+05:30	
40	\N	\N	Chandani Chauk	\N	Delhi	\N	\N	100006	2016-02-03 12:23:22.834675+05:30	
41	\N	\N	Chandani Chauk	\N	\N	\N	India	100006	2016-02-03 12:25:03.861278+05:30	
42	\N	\N	Chandani Chauk	\N	\N	\N	India	100006	2016-02-03 12:25:32.497158+05:30	
43	\N	\N	Chandani Chauk	\N	\N	\N	India	100006	2016-02-03 12:25:39.622569+05:30	
44	\N	\N	Chandani Chauk	\N	\N	\N	India	100006	2016-02-03 12:51:04.12292+05:30	
45	121	test street	Chandani Chauk	Near metro station	Delhi	Delhi	India	100006	2016-02-03 16:24:59.682839+05:30	
\.


--
-- Name: address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('address_id_seq', 45, true);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add access attempt	7	add_accessattempt
20	Can change access attempt	7	change_accessattempt
21	Can delete access attempt	7	delete_accessattempt
22	Can add access log	8	add_accesslog
23	Can change access log	8	change_accesslog
24	Can delete access log	8	delete_accesslog
25	Can add religion	9	add_religion
26	Can change religion	9	change_religion
27	Can delete religion	9	delete_religion
28	Can add address	10	add_address
29	Can change address	10	change_address
30	Can delete address	10	delete_address
31	Can add users	11	add_users
32	Can change users	11	change_users
33	Can delete users	11	delete_users
34	Can add vendors	12	add_vendors
35	Can change vendors	12	change_vendors
36	Can delete vendors	12	delete_vendors
37	Can add vendor_ cordinators	13	add_vendor_cordinators
38	Can change vendor_ cordinators	13	change_vendor_cordinators
39	Can delete vendor_ cordinators	13	delete_vendor_cordinators
40	Can add venue_ types	14	add_venue_types
41	Can change venue_ types	14	change_venue_types
42	Can delete venue_ types	14	delete_venue_types
46	Can add videos	16	add_videos
47	Can change videos	16	change_videos
48	Can delete videos	16	delete_videos
49	Can add venues	17	add_venues
50	Can change venues	17	change_venues
51	Can delete venues	17	delete_venues
52	Can add card_ types	18	add_card_types
53	Can change card_ types	18	change_card_types
54	Can delete card_ types	18	delete_card_types
55	Can add beautician_ types	19	add_beautician_types
56	Can change beautician_ types	19	change_beautician_types
57	Can delete beautician_ types	19	delete_beautician_types
58	Can add music_ types	20	add_music_types
59	Can change music_ types	20	change_music_types
60	Can delete music_ types	20	delete_music_types
61	Can add gift_ types	21	add_gift_types
62	Can change gift_ types	21	change_gift_types
63	Can delete gift_ types	21	delete_gift_types
70	Can add bakery_ types	24	add_bakery_types
71	Can change bakery_ types	24	change_bakery_types
72	Can delete bakery_ types	24	delete_bakery_types
73	Can add ghodi_ bagghi_ types	25	add_ghodi_bagghi_types
74	Can change ghodi_ bagghi_ types	25	change_ghodi_bagghi_types
75	Can delete ghodi_ bagghi_ types	25	delete_ghodi_bagghi_types
76	Can add band_ types	26	add_band_types
77	Can change band_ types	26	change_band_types
78	Can delete band_ types	26	delete_band_types
79	Can add mehendi_ types	27	add_mehendi_types
80	Can change mehendi_ types	27	change_mehendi_types
81	Can delete mehendi_ types	27	delete_mehendi_types
82	Can add fireworks_ types	28	add_fireworks_types
83	Can change fireworks_ types	28	change_fireworks_types
84	Can delete fireworks_ types	28	delete_fireworks_types
85	Can add tent_ types	29	add_tent_types
86	Can change tent_ types	29	change_tent_types
87	Can delete tent_ types	29	delete_tent_types
88	Can add cards	30	add_cards
89	Can change cards	30	change_cards
90	Can delete cards	30	delete_cards
91	Can add cart	31	add_cart
92	Can change cart	31	change_cart
93	Can delete cart	31	delete_cart
94	Can add product_ pictures	32	add_product_pictures
95	Can change product_ pictures	32	change_product_pictures
96	Can delete product_ pictures	32	delete_product_pictures
100	Can add user social auth	34	add_usersocialauth
101	Can change user social auth	34	change_usersocialauth
102	Can delete user social auth	34	delete_usersocialauth
103	Can add nonce	35	add_nonce
104	Can change nonce	35	change_nonce
105	Can delete nonce	35	delete_nonce
106	Can add association	36	add_association
107	Can change association	36	change_association
108	Can delete association	36	delete_association
109	Can add code	37	add_code
110	Can change code	37	change_code
111	Can delete code	37	delete_code
112	Can add wishlist	38	add_wishlist
113	Can change wishlist	38	change_wishlist
114	Can delete wishlist	38	delete_wishlist
115	Can add delivery_ status	39	add_delivery_status
116	Can change delivery_ status	39	change_delivery_status
117	Can delete delivery_ status	39	delete_delivery_status
118	Can add orders	40	add_orders
119	Can change orders	40	change_orders
120	Can delete orders	40	delete_orders
121	Can add rating	41	add_rating
122	Can change rating	41	change_rating
123	Can delete rating	41	delete_rating
124	Can add user rating	42	add_userrating
125	Can change user rating	42	change_userrating
126	Can delete user rating	42	delete_userrating
127	Can add reviews	43	add_reviews
128	Can change reviews	43	change_reviews
129	Can delete reviews	43	delete_reviews
130	Can add card_ colors	44	add_card_colors
131	Can change card_ colors	44	change_card_colors
132	Can delete card_ colors	44	delete_card_colors
133	Can add card_ deities	45	add_card_deities
134	Can change card_ deities	45	change_card_deities
135	Can delete card_ deities	45	delete_card_deities
136	Can add beauticians	46	add_beauticians
137	Can change beauticians	46	change_beauticians
138	Can delete beauticians	46	delete_beauticians
139	Can add cards_ preferences	47	add_cards_preferences
140	Can change cards_ preferences	47	change_cards_preferences
141	Can delete cards_ preferences	47	delete_cards_preferences
142	Can add budget	48	add_budget
143	Can change budget	48	change_budget
144	Can delete budget	48	delete_budget
145	Can add main_ preferences	49	add_main_preferences
146	Can change main_ preferences	49	change_main_preferences
147	Can delete main_ preferences	49	delete_main_preferences
148	Can add photo_ video_ types	50	add_photo_video_types
149	Can change photo_ video_ types	50	change_photo_video_types
150	Can delete photo_ video_ types	50	delete_photo_video_types
151	Can add tax_ and_ refund_ policies	51	add_tax_and_refund_policies
152	Can change tax_ and_ refund_ policies	51	change_tax_and_refund_policies
153	Can delete tax_ and_ refund_ policies	51	delete_tax_and_refund_policies
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 153, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
34	pbkdf2_sha256$20000$ZwJ1kuaR7gL2$ItXlP7TtqBAE2AaS2s6f2efniXL1W2MUIfLfZcOnvyA=	2016-02-03 12:23:57.265804+05:30	f	habibs				f	t	2016-01-21 12:53:14.635268+05:30
1	pbkdf2_sha256$20000$Uv07MPzLXFG4$Zmi88IypstwWkJGNvpswks1oaFPTqx3/nINbCB6x+Hw=	2016-02-06 11:27:53.114214+05:30	t	admin	Abhay	Gupta	iabhaygupta90@gmail.com	t	t	2015-11-28 04:42:53+05:30
12	pbkdf2_sha256$20000$jiabDN42Ah84$WsQygdmxMONijprw5ABTSFtYiTeNr/QzBKoenYeyEcw=	2016-02-13 07:49:55.254646+05:30	f	iabhaygupta90@yahoo.com	Abhay		iabhaygupta90@yahoo.com	f	t	2015-11-29 18:39:44.619304+05:30
35	pbkdf2_sha256$20000$KC5pkpE2Q6BK$0kZbh4REsLPnB4FWExvWxsoG+dmHXVGIdUvuKgAw6fs=	2016-02-15 22:30:41.839318+05:30	f	malhotra				f	t	2016-01-21 12:53:24.94787+05:30
8	pbkdf2_sha256$20000$PBbNVNEPDrb8$HUv1JmZd+2eD94TLoYzBDkPlNW45J+DNbb9XO46wxc4=	\N	f	abhay_test@testmail.com			abhay_test@testmail.com	f	t	2015-11-29 18:09:42.226+05:30
9	pbkdf2_sha256$20000$hluCfXA5ONyl$1QUpR9mPijFP48SyW7RPTYTjCXcQn78D09wz1miMKls=	\N	f	iabhaygupta@yahoo.com			iabhaygupta@yahoo.com	f	t	2015-11-29 18:11:23.669826+05:30
28	!Gu1QrsgD4m7w0k1uFzHlRWDCPRKtCWeqvxSevND5	2016-01-21 12:18:47.367921+05:30	f	AbhayGupta	Abhay	Gupta		f	t	2015-12-06 15:48:31.763649+05:30
29	pbkdf2_sha256$20000$HwO3v0c0YX92$MAW7dJ6kYhjkLxdmVh+6P0CqUcz4zHeFuwtROJ62b/4=	2016-01-21 12:33:38.534468+05:30	f	vendor1				f	t	2016-01-21 12:32:45.323482+05:30
30	pbkdf2_sha256$20000$XOt9ULPDLEPj$oBehfTIFmloQfY+4r6aYctE4KlGlSxHKLIbuDP526Z4=	\N	f	radhikamandapam				f	t	2016-01-21 12:52:14+05:30
32	pbkdf2_sha256$20000$MvNh24MJp5cP$5crbTY3MR+bxi7YqOmO3srd7ntHDfPFdQbsWFOly5z0=	\N	f	ghanshyam				f	t	2016-01-21 12:52:56.877601+05:30
33	pbkdf2_sha256$20000$vRNPPeFydayU$tZIzM8nRaNvnAd3wOY8MrBM9a3lHFp/GytTTeLXwSCc=	\N	f	yoyo				f	t	2016-01-21 12:53:06.327173+05:30
31	pbkdf2_sha256$20000$3ZFfzGmhFCf8$r5gpf7ILq8xEmxyJGx4wH1coV2sik1Ty9LTh0UBwdO4=	2016-01-21 14:40:59.174999+05:30	f	shagun				f	t	2016-01-21 12:52:42.165239+05:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 35, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: axes_accessattempt; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY axes_accessattempt (id, user_agent, ip_address, username, trusted, http_accept, path_info, attempt_time, get_data, post_data, failures_since_start) FROM stdin;
\.


--
-- Name: axes_accessattempt_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('axes_accessattempt_id_seq', 1, false);


--
-- Data for Name: axes_accesslog; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY axes_accesslog (id, user_agent, ip_address, username, trusted, http_accept, path_info, attempt_time, logout_time) FROM stdin;
\.


--
-- Name: axes_accesslog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('axes_accesslog_id_seq', 1, false);


--
-- Data for Name: bakery_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY bakery_types (id, name) FROM stdin;
\.


--
-- Name: bakery_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('bakery_types_id_seq', 1, false);


--
-- Data for Name: band_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY band_types (id, name) FROM stdin;
1	Eve Shift
\.


--
-- Name: band_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('band_types_id_seq', 1, true);


--
-- Data for Name: beautician_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY beautician_types (id, name) FROM stdin;
1	Wedding
2	Prewedding
3	Engagement
4	Sangeet
5	Reception
\.


--
-- Name: beautician_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('beautician_types_id_seq', 6, true);


--
-- Data for Name: beauticians; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY beauticians (id, ref_id, name, short_description, long_description, services, actual_price, discount_rs, discounted_price, female_person_available, home_visit_charge, type_id, vendor_id, gender, home_visit_policy, barati_confidence_perc, "timestamp", discount_perc, address_id) FROM stdin;
2	HBIS12322XY	Habibs Groom makeup	Prewedding Makeup for groom	Perfect touch of professional hands	Shaving, Bleaching, Black Head removal, hair cut, waxing, threading	4000	\N	\N	f	1000	2	4	male	Available only between 10:00 AM and 9:00 PM.	20	2016-01-02 18:11:02.982006+05:30	28	\N
1	HBIS12322XX	Habibs Bridal 	Wedding Makeup for brides to be	Perfect touch of professional hands	Bleaching, waxing, pedicure, manicure, spa, threading, waterproof bridal makeup, hair style, back, neck and hand make up	5000	\N	\N	t	\N	1	4	female	Available only between 10:00 AM and 9:00 PM.	20	2016-01-02 18:11:02.982006+05:30	28	\N
8	BTN_QQ12	Test	test short	test long	Makeup and bla bla	6000	\N	\N	f	2000	3	4	neutral	Not after 10 PM	\N	2016-02-03 12:51:04.256789+05:30	\N	44
9	BTN_QQ14	Test	test short	test long	Makeup and bla bla	5500	\N	\N	f	2000	3	4	neutral	Not after 10 PM	\N	2016-02-03 16:25:00.21564+05:30	\N	45
\.


--
-- Name: beauticians_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('beauticians_id_seq', 9, true);


--
-- Data for Name: budget; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY budget (id, min_master, max_master, min_venue, max_venue, min_card, max_card, min_beautician, max_beautician, min_mehendi, max_mehendi, min_music, max_music, min_gift, max_gift, min_tent, max_tent, user_id) FROM stdin;
2	10000	100000	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	19
\.


--
-- Name: budget_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('budget_id_seq', 2, true);


--
-- Data for Name: card_colors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY card_colors (id, ref_id, color, hexcode, card_id) FROM stdin;
1	TWC123123G1	red	\N	1
2	TWC123123G1	blue	\N	1
3	TWC123123G1	maroon	\N	1
\.


--
-- Name: card_colors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('card_colors_id_seq', 3, true);


--
-- Data for Name: card_deities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY card_deities (id, ref_id, top_deity_name, inner_deity_name, card_id, inner_deity_image_path, top_deity_image_path) FROM stdin;
1	TWC123123G1	ganesha	shiva	1	\N	\N
2	TWC123123G1	krishna	krishna	1	\N	\N
\.


--
-- Name: card_deities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('card_deities_id_seq', 2, true);


--
-- Data for Name: card_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY card_types (id, name) FROM stdin;
1	Traditional Cards
2	Boxed Cards
3	Designer
4	Scroll
5	Picture Cards
6	Theme Cards
7	Recycled Paper Cards
\.


--
-- Name: card_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('card_types_id_seq', 7, true);


--
-- Data for Name: cards; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY cards (id, ref_id, name, short_description, long_description, min_numbers, max_numbers, type_id, vendor_id, actual_price, discount_rs, discounted_price, length, width, weight, printing_price, barati_confidence_perc, "timestamp", discount_perc, address_id) FROM stdin;
1	TWC123123G1	Special Ganesha Card	Exclusive premium wedding card	Banarasi traditional wedding card with embossed Ganesha	100	1000	1	1	25	\N	\N	\N	\N	\N	0.5	\N	2016-01-02 16:59:15.481612+05:30	31	\N
6	CAS12XXDS	Scroll Card	Test scroll card	Long desc of scroll card hahahahaha!	100	1000	4	1	21	\N	\N	\N	\N	\N	0.200000000000000011	23	2016-01-04 01:09:51.793565+05:30	28	\N
2	SC1233XXP1	Shahi Card	Shahi Card with a Royal look	Attractive soft paper, royal color card	200	2000	1	1	28	\N	\N	\N	\N	\N	0.5	\N	2016-01-02 16:59:15.481612+05:30	48	\N
9	xx	x	test short	test long	100	800	2	1	12	\N	\N	12	7	10	\N	\N	2016-02-01 23:40:56.527023+05:30	\N	\N
11	xxy	xy	test short	test long	100	800	2	1	30	\N	\N	12	7	10	\N	\N	2016-02-02 00:25:46.532746+05:30	\N	17
12	xxyz	xxyz	test short	test long	100	800	1	1	28	\N	\N	12	7	10	\N	\N	2016-02-02 01:01:40.375653+05:30	\N	18
\.


--
-- Name: cards_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('cards_id_seq', 12, true);


--
-- Data for Name: cards_preferences; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY cards_preferences (id, ref_id, avail_printing, card_id, user_id) FROM stdin;
3	TWC123123G1	f	1	10
4	CAS12XXDS	t	6	10
2	SC1233XXP1	f	2	19
1	TWC123123G1	t	1	19
\.


--
-- Name: cards_preferences_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('cards_preferences_id_seq', 4, true);


--
-- Data for Name: cart; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY cart (id, ref_id, product_type, checked_out, quantity, user_id, total_price) FROM stdin;
252	HBIS12322XY	beautician	f	1	10	5400
253	CAS12XXDS	card	f	100	10	2420
255	HBIS12322XX	beautician	f	1	19	6750
256	SC1233XXP1	card	f	1	19	31.5
258	TWC123123G1	card	f	100	19	2863
\.


--
-- Name: cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('cart_id_seq', 258, true);


--
-- Data for Name: delivery_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY delivery_status (id, ref_id, name, status, link, "timestamp", order_id) FROM stdin;
28	HBIS12322XY	Delhivery	Not yet handed over	http://google.com	2016-01-09 11:59:03.5619+05:30	106
29	TWC123123G1	Delhivery	Not yet handed over	http://google.com	2016-01-09 11:59:03.714077+05:30	107
30	TWC123123G1	Delhivery	Not yet handed over	http://google.com	2016-01-09 11:59:03.736107+05:30	108
31	TWC123123G1	Delhivery	Not yet handed over	http://google.com	2016-01-09 11:59:03.758351+05:30	109
32	TWC123123G1	Delhivery	Not yet handed over	http://google.com	2016-01-09 11:59:03.780595+05:30	110
33	TWC123123G1	Delhivery	Not yet handed over	http://google.com	2016-01-09 11:59:03.802934+05:30	111
34	SC1233XXP1	Delhivery	Not yet handed over	http://google.com	2016-01-09 11:59:03.825175+05:30	112
35	HBIS12322XX	Delhivery	Not yet handed over	http://google.com	2016-01-09 11:59:03.847501+05:30	113
36	TWC123123G1	Delhivery	Not yet handed over	http://google.com	2016-01-10 16:06:20.477838+05:30	114
\.


--
-- Name: delivery_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('delivery_status_id_seq', 36, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2015-11-29 18:41:46.86906+05:30	1	AbhayGupta	3		34	1
2	2015-12-06 10:45:44.8596+05:30	10	admin	1		11	1
3	2015-12-06 10:46:41.042277+05:30	1	admin	2	Changed first_name and last_name.	4	1
4	2015-12-06 14:09:40.547441+05:30	2	AbhayGupta1ffa0157a3b44e0d	3		34	1
5	2015-12-06 14:09:53.033153+05:30	13	AbhayGupta1ffa0157a3b44e0d	3		4	1
6	2015-12-06 14:21:05.82344+05:30	2	AbhayGupta	3		4	1
7	2015-12-06 14:21:13.511958+05:30	14	AbhayGuptaa9f48ff78d934640	3		4	1
8	2015-12-06 14:25:35.244125+05:30	15	AbhayGupta	3		4	1
9	2015-12-06 14:33:58.243312+05:30	16	AbhayGupta	3		4	1
10	2015-12-06 14:37:46.043494+05:30	17	AbhayGupta	3		4	1
11	2015-12-06 14:40:48.12143+05:30	18	AbhayGupta	3		4	1
12	2015-12-06 15:18:53.519525+05:30	19	AbhayGupta	3		4	1
13	2015-12-06 15:31:31.471238+05:30	21	AbhayGupta	3		4	1
14	2015-12-06 15:31:43.613819+05:30	12	AbhayGupta	3		11	1
15	2015-12-06 15:34:53.121023+05:30	22	AbhayGupta	3		4	1
16	2015-12-06 15:35:05.434492+05:30	13	AbhayGupta	3		11	1
17	2015-12-06 15:36:25.02845+05:30	23	AbhayGupta	3		4	1
18	2015-12-06 15:36:34.892559+05:30	14	AbhayGupta	3		11	1
19	2015-12-06 15:38:52.678072+05:30	24	AbhayGupta	3		4	1
20	2015-12-06 15:39:01.433608+05:30	15	AbhayGupta	3		11	1
21	2015-12-06 15:40:13.761047+05:30	17	aa@c.c.c.c	3		11	1
22	2015-12-06 15:40:33.230637+05:30	26	aa@c.c.c.c	3		4	1
23	2015-12-06 15:46:43.311155+05:30	25	AbhayGupta	3		4	1
24	2015-12-06 15:47:00.219803+05:30	16	AbhayGupta	3		11	1
25	2015-12-06 15:48:08.48844+05:30	27	AbhayGupta	3		4	1
26	2015-12-06 15:48:18.866104+05:30	18	AbhayGupta	3		11	1
27	2015-12-10 21:55:28.564859+05:30	1	Traditional Cards	1		21	1
28	2015-12-10 21:55:37.268148+05:30	2	Boxed Cards	1		21	1
29	2015-12-10 21:55:47.504094+05:30	3	Designer Cards	1		21	1
30	2015-12-10 21:55:55.582715+05:30	4	Scrolls	1		21	1
31	2015-12-10 21:56:03.325255+05:30	5	Picture Cards	1		21	1
32	2015-12-10 21:56:16.093419+05:30	6	Theme Based Cards	1		21	1
33	2015-12-10 21:56:32.870933+05:30	7	Nature Friendly Cards	1		21	1
34	2015-12-10 21:56:47.12807+05:30	7	Nature Friendly Cards	3		21	1
35	2015-12-10 21:56:47.140152+05:30	6	Theme Based Cards	3		21	1
36	2015-12-10 21:56:47.151293+05:30	5	Picture Cards	3		21	1
37	2015-12-10 21:56:47.162345+05:30	4	Scrolls	3		21	1
38	2015-12-10 21:56:47.173434+05:30	3	Designer Cards	3		21	1
39	2015-12-10 21:56:47.184416+05:30	2	Boxed Cards	3		21	1
40	2015-12-10 21:56:47.195943+05:30	1	Traditional Cards	3		21	1
41	2015-12-10 22:00:09.69387+05:30	1	Wedding	1		19	1
42	2015-12-10 22:00:15.012578+05:30	2	Prewedding	1		19	1
43	2015-12-10 22:00:19.557058+05:30	3	Reception	1		19	1
44	2015-12-10 22:00:32.004533+05:30	4	Engagement	1		19	1
45	2015-12-10 22:00:36.998081+05:30	5	Sangeet	1		19	1
46	2015-12-10 22:00:46.138396+05:30	6	Reception	1		19	1
47	2015-12-10 22:01:04.945795+05:30	3	Reception	3		19	1
48	2015-12-10 22:50:17.613529+05:30	2	Chhatarpur	1		10	1
49	2015-12-10 22:52:12.688559+05:30	4	Habibs	1		12	1
50	2015-12-10 22:58:47.253598+05:30	1	HBIS12322XX	1		46	1
51	2015-12-10 23:01:59.32719+05:30	2	HBIS12322XY	1		46	1
52	2015-12-10 23:10:00.817146+05:30	2	HBIS12322XY	2	Changed gender.	46	1
53	2015-12-10 23:10:09.27258+05:30	1	HBIS12322XX	2	Changed gender.	46	1
54	2015-12-10 23:49:36.586649+05:30	3	HBIS12322XY	1		32	1
55	2015-12-10 23:50:00.485646+05:30	4	HBIS12322XX	1		32	1
56	2015-12-10 23:52:01.491754+05:30	4	HBIS12322XX	2	Changed picture_path.	32	1
57	2015-12-10 23:52:07.947632+05:30	3	HBIS12322XY	2	Changed picture_path.	32	1
58	2015-12-12 04:06:21.918816+05:30	2	HBIS12322XY	2	Changed short_description.	46	1
59	2015-12-13 00:27:11.236133+05:30	2	HBIS12322XY	2	Changed female_person_available.	46	1
60	2015-12-13 00:27:58.801528+05:30	2	HBIS12322XY	2	Changed female_person_available.	46	1
61	2016-01-04 01:09:52.536973+05:30	6	CAS12XXDS	1		30	1
62	2016-01-04 01:17:19.159569+05:30	5	CAS12XXDS.jpg	1		32	1
63	2016-01-04 01:18:40.020231+05:30	5	CAS12XXDS	2	Changed ref_id.	32	1
64	2016-01-04 01:19:57.01894+05:30	5	CAS12XXDS	2	Changed picture_path.	32	1
65	2016-01-05 22:58:20.354511+05:30	5	YoYo Tent House	1		12	1
66	2016-01-05 22:58:40.399642+05:30	6	Ghanshyam Tent House	1		12	1
67	2016-01-05 23:00:10.988707+05:30	7	Shagun Marriage Garden	1		12	1
68	2016-01-05 23:00:35.280807+05:30	8	Radhika Mandapam	1		12	1
69	2016-01-05 23:03:43.976885+05:30	1	Shagun Marriage Garden	1		17	1
70	2016-01-05 23:05:04.847175+05:30	2	Radhika Mandapam	1		17	1
71	2016-01-05 23:11:46.553382+05:30	6	VN2213SW	1		32	1
72	2016-01-05 23:12:13.598211+05:30	7	VN123AQ	1		32	1
73	2016-01-06 22:53:49.393575+05:30	8	Personalized	1		21	1
74	2016-01-06 22:54:00.095824+05:30	9	Reception	1		21	1
75	2016-01-06 22:54:15.142328+05:30	10	For Baratis	1		21	1
76	2016-01-06 22:54:20.429073+05:30	11	For Her	1		21	1
77	2016-01-06 22:54:25.318525+05:30	12	For Him	1		21	1
82	2016-01-06 22:59:14.74309+05:30	1	Candid	1		50	1
83	2016-01-06 22:59:24.876399+05:30	2	Prewedding	1		50	1
84	2016-01-06 22:59:28.237559+05:30	3	Wedding	1		50	1
85	2016-01-06 22:59:32.247391+05:30	4	Just Married	1		50	1
86	2016-01-09 12:08:59.674336+05:30	1	Eve Shift	1		26	1
87	2016-01-12 23:23:57.15083+05:30	2	card	1		51	1
88	2016-01-13 00:03:43.102441+05:30	2	card	2	Changed refund_after_die_preparing.	51	1
89	2016-01-13 00:05:46.38923+05:30	3	beautician	1		51	1
90	2016-01-13 00:06:38.959229+05:30	4	ghodi_bagghi	1		51	1
91	2016-01-13 00:07:58.978806+05:30	2	card	2	Changed refund_within_2_days, refund_between_2_7_days, refund_between_7_15_days and refund_between_15_30_days.	51	1
92	2016-01-13 21:53:05.906605+05:30	5	venue	1		51	1
93	2016-01-21 12:13:18.867614+05:30	10	admin	2	Changed role.	11	1
94	2016-01-21 12:13:55.884947+05:30	20	vendor1	1		11	1
95	2016-01-21 12:32:29.99942+05:30	20	vendor1	3		11	1
96	2016-01-21 12:32:45.447166+05:30	29	vendor1	1		4	1
97	2016-01-21 12:52:14.748798+05:30	30	radhikamandapam	1		4	1
98	2016-01-21 12:52:21.444088+05:30	30	radhikamandapam	2	No fields changed.	4	1
99	2016-01-21 12:52:42.193688+05:30	31	shagun	1		4	1
100	2016-01-21 12:52:56.911485+05:30	32	ghanshyam	1		4	1
101	2016-01-21 12:53:06.358708+05:30	33	yoyo	1		4	1
102	2016-01-21 12:53:14.669956+05:30	34	habibs	1		4	1
103	2016-01-21 12:53:24.981163+05:30	35	malhotra	1		4	1
104	2016-01-21 12:54:02.476087+05:30	8	Radhika Mandapam	2	Changed user.	12	1
105	2016-01-21 12:54:09.316278+05:30	7	Shagun Marriage Garden	2	Changed user.	12	1
106	2016-01-21 12:54:15.715916+05:30	6	Ghanshyam Tent House	2	Changed user.	12	1
107	2016-01-21 12:54:51.51087+05:30	4	Habibs	2	Changed user.	12	1
108	2016-01-21 12:54:56.104229+05:30	1	Malhotra Cards	2	Changed user.	12	1
109	2016-01-21 12:55:06.11614+05:30	5	YoYo Tent House	2	Changed user.	12	1
110	2016-01-21 17:22:52.223711+05:30	3	12 JL Road Chandani Chawk	1		10	1
111	2016-02-06 11:30:12.993951+05:30	65	VN2213SW	1		32	1
112	2016-02-06 11:30:39.204714+05:30	66	VN123AQ	1		32	1
113	2016-02-06 11:36:06.282388+05:30	52	HBIS12322XY	2	Changed name.	32	1
114	2016-02-07 21:32:24.44158+05:30	52	HBIS12322XY	2	Changed picture.	32	1
115	2016-02-07 21:33:03.957945+05:30	52	HBIS12322XY	2	Changed picture.	32	1
116	2016-02-07 21:33:31.608226+05:30	52	HBIS12322XY	2	Changed picture.	32	1
117	2016-02-07 21:33:40.488247+05:30	52	HBIS12322XY	2	Changed picture.	32	1
118	2016-02-07 21:33:59.147701+05:30	52	HBIS12322XY	2	Changed picture.	32	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 118, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	axes	accessattempt
8	axes	accesslog
9	customers	religion
10	customers	address
11	customers	users
12	customers	vendors
13	customers	vendor_cordinators
14	customers	venue_types
16	customers	videos
17	customers	venues
18	customers	card_types
19	customers	beautician_types
20	customers	music_types
21	customers	gift_types
24	customers	bakery_types
25	customers	ghodi_bagghi_types
26	customers	band_types
27	customers	mehendi_types
28	customers	fireworks_types
29	customers	tent_types
30	customers	cards
31	customers	cart
32	customers	product_pictures
34	default	usersocialauth
35	default	nonce
36	default	association
37	default	code
38	customers	wishlist
39	customers	delivery_status
40	customers	orders
41	star_ratings	rating
42	star_ratings	userrating
43	customers	reviews
44	customers	card_colors
45	customers	card_deities
46	customers	beauticians
47	customers	cards_preferences
48	customers	budget
49	customers	main_preferences
50	customers	photo_video_types
51	customers	tax_and_refund_policies
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 51, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
102	customers	0001_initial	2016-01-14 14:30:08.965296+05:30
103	customers	0002_auto_20160114_1430	2016-01-14 14:30:42.377693+05:30
104	contenttypes	0001_initial	2016-01-14 14:32:09.975236+05:30
105	auth	0001_initial	2016-01-14 14:32:10.036664+05:30
106	admin	0001_initial	2016-01-14 14:32:10.060495+05:30
107	contenttypes	0002_remove_content_type_name	2016-01-14 14:33:39.619929+05:30
108	auth	0002_alter_permission_name_max_length	2016-01-14 14:33:39.663524+05:30
109	auth	0003_alter_user_email_max_length	2016-01-14 14:33:39.696849+05:30
110	auth	0004_alter_user_username_opts	2016-01-14 14:33:39.719223+05:30
111	auth	0005_alter_user_last_login_null	2016-01-14 14:33:39.743174+05:30
112	auth	0006_require_contenttypes_0002	2016-01-14 14:33:39.752117+05:30
113	default	0001_initial	2016-01-14 14:33:39.810936+05:30
114	default	0002_add_related_name	2016-01-14 14:33:40.210174+05:30
115	default	0003_alter_email_max_length	2016-01-14 14:33:40.267483+05:30
116	sessions	0001_initial	2016-01-14 14:33:40.298592+05:30
117	star_ratings	0001_initial	2016-01-14 14:33:40.408039+05:30
118	customers	0003_orders_vendor	2016-01-15 14:08:33.971453+05:30
119	customers	0004_users_role	2016-01-21 12:12:43.967088+05:30
120	customers	0005_vendors_user	2016-01-21 12:49:57.365186+05:30
121	customers	0006_address_type	2016-01-21 14:40:02.994054+05:30
122	customers	0007_auto_20160128_1035	2016-01-28 10:35:09.592484+05:30
123	customers	0008_auto_20160129_1305	2016-01-29 13:11:09.828214+05:30
124	customers	0009_remove_venues_alcohol_serving	2016-01-29 13:11:10.205939+05:30
125	customers	0010_venues_alcohol_serving	2016-01-29 13:11:10.27264+05:30
126	customers	0002_auto_20160201_1626	2016-02-01 16:27:03.622545+05:30
127	customers	0003_auto_20160201_2259	2016-02-01 22:59:07.688847+05:30
128	customers	0004_auto_20160201_2314	2016-02-01 23:14:24.147191+05:30
129	customers	0005_auto_20160201_2319	2016-02-01 23:19:36.002192+05:30
130	customers	0006_auto_20160201_2347	2016-02-01 23:47:16.273402+05:30
131	customers	0007_auto_20160202_1107	2016-02-02 11:11:57.309063+05:30
132	customers	0008_remove_venues_alcohol_serving	2016-02-03 11:35:41.531963+05:30
133	customers	0009_venues_alcohol_serving	2016-02-03 11:36:00.876844+05:30
134	customers	0010_auto_20160203_1250	2016-02-03 12:50:57.982488+05:30
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 134, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
q32ga6k7s0bxz326bv163fc7fj0orxrt	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-12-20 14:37:28.523261+05:30
vvnktgz8k1ncd4p568m727l7gsmyna9z	ZWE1NWQxMDc2MDVkNjQzZmI2ZGY3MDg0ZTIzYjBkYWQyYzg1MTZiODp7ImZhY2Vib29rX3N0YXRlIjoiVjZ6bUFRSVNqYUJ4R2o3cE1CUXMyejYwRkNZVHk4Y3oiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJmYWNlYm9vayIsIl9hdXRoX3VzZXJfaGFzaCI6ImZmMjdkYTY0Njc3MmI4NDkzMzMwMzk0ODdlNDM3ZDg1ZTJlNjY5NTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJfYXV0aF91c2VyX2lkIjoiMjgifQ==	2016-01-13 11:52:40.791899+05:30
4l9wu6lh4xlf3oq06zoexxijlpqmrz7b	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-12-27 00:26:59.530301+05:30
4bszxhvh6t27v61w9a4lzpjzb8ad74cu	ZTRjMTlhMmE1NjU4NDRmOWM5MjRkNWU1YjNkNWZiMDEwOWE3MDZmMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsImZhY2Vib29rX3N0YXRlIjoiTHg0dGN4OGVhbzY0Z0tYckFoUXU2aERSN2VSZ2dqOVQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJuZXh0IjoiL2F1dGgvbG9naW4vIiwic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoiZmFjZWJvb2siLCJfYXV0aF91c2VyX2hhc2giOiJmZjI3ZGE2NDY3NzJiODQ5MzMzMDM5NDg3ZTQzN2Q4NWUyZTY2OTUzIn0=	2016-01-05 10:39:47.183408+05:30
5bzo7puczznmelmfdhnqgwpm5s7vkg2e	NzFmNDlmMzkwNTcwYjM5MjlhZWI0NTlkMzA3OTNiNzlhNTI0YTAyMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsImZhY2Vib29rX3N0YXRlIjoieEVzTE1JY0s3SzdHRVp2b3RWdjFyRHFCV1JYc1lKZXgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJuZXh0IjoiL2F1dGgvbG9naW4vIiwic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoiZmFjZWJvb2siLCJfYXV0aF91c2VyX2hhc2giOiJmZjI3ZGE2NDY3NzJiODQ5MzMzMDM5NDg3ZTQzN2Q4NWUyZTY2OTUzIn0=	2015-12-20 22:16:14.834895+05:30
z3f8xkuelc4ujiflh1akwkrkdqn2vszh	NmQyOTAxMDQ1ZDkyODIwNTExNGQ2N2VmMjhkYTJhNjIxZjVlYzhkYjp7ImZhY2Vib29rX3N0YXRlIjoiOUh5VTNIQVJvRVY1UGc1NmFLS201UzNTZ1RranhTc0giLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJmYWNlYm9vayIsIl9hdXRoX3VzZXJfaGFzaCI6ImZmMjdkYTY0Njc3MmI4NDkzMzMwMzk0ODdlNDM3ZDg1ZTJlNjY5NTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJfYXV0aF91c2VyX2lkIjoiMjgifQ==	2016-01-16 17:55:05.907011+05:30
qs1heg0cujxovaq8iv3e82dp3ufz7jqg	ZTZhYWUwZTZlNTU1MWI1YjdjMTZhMGI4YjhhNzcxMWZjYzkwODk3Mzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsImZhY2Vib29rX3N0YXRlIjoiUm82UG9ucklkZjM4bjlkSld1QlcyM3l6TWxXM2MzakYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJuZXh0IjoiL2F1dGgvbG9naW4vIiwic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoiZmFjZWJvb2siLCJfYXV0aF91c2VyX2hhc2giOiJmZjI3ZGE2NDY3NzJiODQ5MzMzMDM5NDg3ZTQzN2Q4NWUyZTY2OTUzIn0=	2016-01-11 20:32:16.666111+05:30
4zj7n1mdbgyxflqq2atg3l621fo07bdm	ODMzYjU1MTlhMjg1YzNkYTdlYTZhNWU4ZjM3NjE5NDk5YWI4NmU2ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjI5YzNmMWMzZGVlOTExYzc1M2JiODY2ZTQ2MzZjNDFiMTI3MDM4NTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9	2015-12-13 22:50:42.750272+05:30
rf663ean5nuc07i2vzzclheq9cinilk3	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-01-18 00:56:48.752936+05:30
96n2zl2bk2g4pmwhgwvk033yylbzg42x	ODMzYjU1MTlhMjg1YzNkYTdlYTZhNWU4ZjM3NjE5NDk5YWI4NmU2ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjI5YzNmMWMzZGVlOTExYzc1M2JiODY2ZTQ2MzZjNDFiMTI3MDM4NTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9	2015-12-15 10:38:55.884763+05:30
a3xbxpvvnkytk4eni3ue2c8n84utrmh8	OTk3YWY0ZWRjZWQxZWNiYjAwZTQ4NzgzN2RjMGNlYWE1Yzg3OGE0ZTp7ImZhY2Vib29rX3N0YXRlIjoiUXlLeU5uM1ZEeUFqbnEzdVQ2MmRXcm80cjZyT2JLVnEiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJmYWNlYm9vayIsIl9hdXRoX3VzZXJfaGFzaCI6ImZmMjdkYTY0Njc3MmI4NDkzMzMwMzk0ODdlNDM3ZDg1ZTJlNjY5NTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJfYXV0aF91c2VyX2lkIjoiMjgifQ==	2016-01-18 22:39:15.686455+05:30
verry1eet67c4nb0akimjle8yunk6wr5	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-01-20 14:31:25.079492+05:30
k6kd7lisso125u1ldwrzfcl7c17z5f02	ODMzYjU1MTlhMjg1YzNkYTdlYTZhNWU4ZjM3NjE5NDk5YWI4NmU2ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjI5YzNmMWMzZGVlOTExYzc1M2JiODY2ZTQ2MzZjNDFiMTI3MDM4NTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9	2015-12-16 00:59:37.988907+05:30
8f78b81tn321zr34gm2089vgk41roobd	MDhjYzYzZWE5MzU3NTNlZjlhNzg4ZDQzNDBlOWE5MjJjMjA2MjhjYzp7ImZhY2Vib29rX3N0YXRlIjoidzZjQ2ZTWFQwTWdVcDBjR2lCUFgxV2dzUnpDOFM3bEciLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJmYWNlYm9vayIsIl9hdXRoX3VzZXJfaGFzaCI6ImZmMjdkYTY0Njc3MmI4NDkzMzMwMzk0ODdlNDM3ZDg1ZTJlNjY5NTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJfYXV0aF91c2VyX2lkIjoiMjgifQ==	2016-01-20 22:49:20.902784+05:30
p8cfgbdx3m2eiuspnejp1f8wcn1te9c0	ZWQyMDRhNWY0ZGVlNTg4MTZlN2ZhNDdmYjhlNDlhNmY3NjMxNTE0Yzp7ImZhY2Vib29rX3N0YXRlIjoiUkVHcjBtVEtySXZxeURsZm52c0dvTXBwV2lDMm5oY0QiLCJuZXh0IjoiL2F1dGgvbG9naW4vIn0=	2015-12-24 21:34:56.261557+05:30
cvpktvvf77zhpgchy2it65s1mv372xao	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2015-12-24 21:55:01.625553+05:30
ox3j2i8b0phjjud3wvkdsxqoz8g2c1zn	N2VlOGI2Y2U4OTg0YzA3NGRhNGRmNzhhNGUyODQwZGE4ZWQxMTVlYzp7ImZhY2Vib29rX3N0YXRlIjoiTGJKZ0F3Wmp3b3d6cUpOMk90MEx0d25MdFU1WDFqQU0iLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJmYWNlYm9vayIsIl9hdXRoX3VzZXJfaGFzaCI6ImZmMjdkYTY0Njc3MmI4NDkzMzMwMzk0ODdlNDM3ZDg1ZTJlNjY5NTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJfYXV0aF91c2VyX2lkIjoiMjgifQ==	2016-01-24 15:55:03.187524+05:30
4clv3apfgs01uoa38zi84xetcq2mprml	MTczYjE1MTM2MzZjNzg5MjJjMDJiM2IzODEwZjExMmVlNDg1ZDgyZDp7ImZhY2Vib29rX3N0YXRlIjoiQkplektNTW83SFEzS2d5M3MwYWl1TXhPc0hIMVJwRWEiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJmYWNlYm9vayIsIl9hdXRoX3VzZXJfaGFzaCI6ImZmMjdkYTY0Njc3MmI4NDkzMzMwMzk0ODdlNDM3ZDg1ZTJlNjY5NTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJzb2NpYWwuYmFja2VuZHMuZmFjZWJvb2suRmFjZWJvb2tPQXV0aDIiLCJfYXV0aF91c2VyX2lkIjoiMjgifQ==	2016-01-26 11:16:56.776536+05:30
ohmcyjgf8jhd7d11qkruajzhe1u460c8	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-01-26 23:19:05.928304+05:30
tkaojfpxx7y0un6g3gtpp0z16pw0cgm9	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-02-04 17:20:32.22892+05:30
dgc4hypryhefl3cl6sgfa84ljofllxdw	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-01-28 14:34:03.679642+05:30
ognz3jkdmmhj3ohjsx58vb1ywlylrv3w	MDIzYTkzMTcxMTc0Njc0NWE1NGVmMGFkYzdkMTRlMmE4ZjFkM2NjOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjI2YTJkMTk3ZmUxOGI2N2I5MjRkZWY1MDAyYmVmY2Y2ODBjYTFmMzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzNCJ9	2016-02-10 14:26:13.821547+05:30
oyoexmcy47mi230znpf0ztyaqtde5lmn	MDIzYTkzMTcxMTc0Njc0NWE1NGVmMGFkYzdkMTRlMmE4ZjFkM2NjOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjI2YTJkMTk3ZmUxOGI2N2I5MjRkZWY1MDAyYmVmY2Y2ODBjYTFmMzEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzNCJ9	2016-02-17 12:23:57.277126+05:30
4eaw32gwprr2sznaeqji68jn2p1mftce	ODhjMzAyZWRhZGYxMThkNGMzYzQ4ZGU3Y2Q5Njg0YTk5ZDQyMmU2MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NTIyOGNmMDAwZDFkMjE1ODliNTZkNjkxOTMxNTI4ZjAxM2JmNjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-02-20 11:27:53.137657+05:30
dj7k2gjm80x7r3uojonn8w5vui67kc7j	OWE4OTc0ODg4NTkzN2FiZGVjNGM5MjNhNWFmODkxMTdjY2Q0ODBiYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ4ZWMyZWMyN2I5ZTBmYWQyY2EyZDJjY2QwMGE3OGIwYTEyMDdjMWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzNSJ9	2016-02-29 22:30:41.906333+05:30
\.


--
-- Data for Name: fireworks_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY fireworks_types (id, name) FROM stdin;
\.


--
-- Name: fireworks_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('fireworks_types_id_seq', 1, false);


--
-- Data for Name: ghodi_bagghi_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ghodi_bagghi_types (id, name) FROM stdin;
\.


--
-- Name: ghodi_bagghi_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ghodi_bagghi_types_id_seq', 1, false);


--
-- Data for Name: gift_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY gift_types (id, name) FROM stdin;
8	Personalized
9	Reception
10	For Baratis
11	For Her
12	For Him
\.


--
-- Name: gift_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('gift_types_id_seq', 12, true);


--
-- Data for Name: main_preferences; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY main_preferences (id, date, location, sublocation, user_id) FROM stdin;
14	2016-01-23	Delhi	Chhatarpur	19
15	\N	Delhi	test locality	9
\.


--
-- Name: main_preferences_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('main_preferences_id_seq', 15, true);


--
-- Data for Name: mehendi_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mehendi_types (id, name) FROM stdin;
\.


--
-- Name: mehendi_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('mehendi_types_id_seq', 1, false);


--
-- Data for Name: music_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY music_types (id, name) FROM stdin;
\.


--
-- Name: music_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('music_types_id_seq', 1, false);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY orders (order_id, ref_id, quantity, total_price, package_id, vendor_acknowledgement, payment_done, payment_received, payment_method, product_type, "timestamp", address_id, user_id, vendor_id, comment, last_status_time) FROM stdin;
107	TWC123123G1	250	6250	card_TWC123123G1_1452320943.7	active	t	t	credit_card	card	2016-01-09 11:59:03.703586+05:30	3	19	1	\N	2016-02-15 22:33:30.712787+05:30
112	SC1233XXP1	1	28	card_SC1233XXP1_1452320943.81	pending	t	t	credit_card	card	2016-01-09 11:59:03.814304+05:30	3	19	\N	\N	\N
108	TWC123123G1	1	25	card_TWC123123G1_1452320943.72	pending	t	t	credit_card	card	2016-01-09 11:59:03.725251+05:30	3	19	1	\N	\N
109	TWC123123G1	14	350	card_TWC123123G1_1452320943.75	pending	t	t	credit_card	card	2016-01-09 11:59:03.747615+05:30	3	19	1	\N	\N
110	TWC123123G1	1	25.5	card_TWC123123G1_1452320943.77	pending	t	t	credit_card	card	2016-01-09 11:59:03.769795+05:30	3	19	1	\N	\N
111	TWC123123G1	1	25.5	card_TWC123123G1_1452320943.79	pending	t	t	credit_card	card	2016-01-09 11:59:03.792038+05:30	3	19	1	\N	\N
114	TWC123123G1	1	25	card_TWC123123G1_1452422180.21	pending	t	t	credit_card	card	2016-01-10 16:06:20.213977+05:30	3	19	1	\N	\N
113	HBIS12322XX	1	5000	beautician_HBIS12322XX_1452320943.84	pending	t	t	credit_card	beautician	2016-01-09 11:59:03.836559+05:30	3	19	4	\N	\N
106	HBIS12322XY	1	4000	beautician_HBIS12322XY_1452320943.33	completed	t	t	credit_card	beautician	2016-01-09 11:59:03.33324+05:30	3	19	4	\N	2016-01-28 14:44:30.793032+05:30
\.


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('orders_id_seq', 114, true);


--
-- Data for Name: photo_video_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY photo_video_types (id, name) FROM stdin;
1	Candid
2	Prewedding
3	Wedding
4	Just Married
\.


--
-- Data for Name: product_pictures; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY product_pictures (id, name, ref_id, picture_path, picture) FROM stdin;
22	B4dmHZjCYAAyKvO.jpg:large.jpeg	xx	cards/xx	cards/xx/B4dmHZjCYAAyKvO.jpg:large.jpeg
24	Snow_man_Wallpaper-20121.jpg	xx	beauticians/xx	beauticians/xx/Snow_man_Wallpaper-20121.jpg
25	lovely-christmas-santa-claus-wallpaper.jpg	xx	beauticians/xx	beauticians/xx/lovely-christmas-santa-claus-wallpaper.jpg
52	HBIS12322XY_1	HBIS12322XY	beauticians/HBIS12322XY	beauticians/HBIS12322XY/HBIS12322XY_1_02z5NhO.jpg
29	CAS12XXDS_1	CAS12XXDS	cards/CAS12XXDS	cards/CAS12XXDS/CAS12XXDS.jpg
28	TWC123123G1_1	TWC123123G1	cards/TWC123123G1	cards/TWC123123G1/TWC123123G1.jpg
30	SC1233XXP1_1	SC1233XXP1	cards/SC1233XXP1	cards/SC1233XXP1/SC1233XXP1.jpg
36	xxyz_1	xxyz	cards/xxyz	cards/xxyz/mota_ru_9121611-1920x1080.jpg
37	xxyz_2	xxyz	cards/xxyz	cards/xxyz/1293041502-secret-santa-bw.jpg
38	xxyz_3	xxyz	cards/xxyz	cards/xxyz/1293041502-secret-santa-bw1.jpg
39	xxyz_additional_1	xxyz	cards/xxyz	cards/xxyz/9acaf3099b65f9dacaf6542e2e8276a2.jpg
40	xxyz_additional_2	xxyz	cards/xxyz	cards/xxyz/9acaf3099b65f9dacaf6542e2e8276a2122.jpg
41	xxyz_additional_3	xxyz	cards/xxyz	cards/xxyz/Untitled.xcf
23	B4dmHZjCYAAyKvO.jpg:large_2.jpeg	xx	beauticians/xx	beauticians/xx/B4dmHZjCYAAyKvO.jpg:large.jpeg
42	VEN_CCVV2_1	CCVV2	venues/CCVV2	venues/CCVV2/hubble_friday_09102015.jpg
43	VEN_CCVV2_2	CCVV2	venues/CCVV2	venues/CCVV2/iss044e095609_0.jpg
44	VEN_CCVV2_3	CCVV2	venues/CCVV2	venues/CCVV2/hs-2015-29-a-xlarge_web.jpg
45	VEN_CCVV2_additional_1	CCVV2	venues/CCVV2	venues/CCVV2/pia19916-main_perspective_2.jpg
46	VEN_CCVV2_additional_2	CCVV2	venues/CCVV2	venues/CCVV2/congratulation_free_wallpapers_9313409645.png
47	VEN_CCVV2_additional_3	CCVV2	venues/CCVV2	venues/CCVV2/phoenix.jpg
48	BTN_QQ12_1	QQ12	beauticians/QQ12	beauticians/QQ12/pia19807_flat-horizon-monday.jpg
49	BTN_QQ12_2	QQ12	beauticians/QQ12	beauticians/QQ12/hubble_friday_08212015.jpg
50	QQ12_additional_1	QQ12	beauticians/QQ12	beauticians/QQ12/solarworlds_crescentmoon_1280x1024copy.jpg
51	QQ12_additional_2	QQ12	beauticians/QQ12	beauticians/QQ12/keep_calm_and_c_on_t_shirt_programmer_code_tee-rebc219c906434195b48253c_goyzS78.jpg
53	BTN_QQ14_1	QQ14	beauticians/QQ14	beauticians/QQ14/B4dmHZjCYAAyKvO.jpg:large.jpeg
54	BTN_QQ14_2	QQ14	beauticians/QQ14	beauticians/QQ14/Snow_man_Wallpaper-20121.jpg
55	BTN_QQ14_3	QQ14	beauticians/QQ14	beauticians/QQ14/lovely-christmas-santa-claus-wallpaper.jpg
56	BTN_QQ14_4	QQ14	beauticians/QQ14	beauticians/QQ14/djed_mraz.jpg
57	BTN_QQ14_5	QQ14	beauticians/QQ14	beauticians/QQ14/widescreen-christmas-background-custom-mikro-plant-322512.jpg
58	BTN_QQ14_6	QQ14	beauticians/QQ14	beauticians/QQ14/mota_ru_9121611-1920x1080.jpg
59	BTN_QQ14_7	QQ14	beauticians/QQ14	beauticians/QQ14/1293041502-secret-santa-bw.jpg
60	BTN_QQ14_8	QQ14	beauticians/QQ14	beauticians/QQ14/1293041502-secret-santa-bw1.jpg
61	BTN_QQ14_9	QQ14	beauticians/QQ14	beauticians/QQ14/s-SECRET-SANTA-RULES-large.jpg
62	QQ14_additional_1	QQ14	beauticians/QQ14	beauticians/QQ14/9acaf3099b65f9dacaf6542e2e8276a2.jpg
63	QQ14_additional_2	QQ14	beauticians/QQ14	beauticians/QQ14/9acaf3099b65f9dacaf6542e2e8276a2122.jpg
64	QQ14_additional_3	QQ14	beauticians/QQ14	beauticians/QQ14/Untitled.xcf
65	VN2213SW_1	VN2213SW	venues/VN2213SW	venues/VN2213SW/VN2213SW_l0eOHGP.jpg
66	VN123AQ_1	VN123AQ	venues/VN123AQ	venues/VN123AQ/VN123AQ_hLujzFo.jpg
\.


--
-- Name: product_pictures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('product_pictures_id_seq', 66, true);


--
-- Data for Name: religion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY religion (id, name) FROM stdin;
\.


--
-- Name: religion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('religion_id_seq', 1, false);


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY reviews (id, ref_id, "timestamp", title, detailed_review, recommended, user_id) FROM stdin;
2	TWC123123G1	2015-12-06 21:07:40.973851+05:30	Awesome product	test	yes	19
3	TWC123123G1	2015-12-06 21:36:46.185294+05:30	Delivery was late but overall a good experience :)	Thanks to Barati for making such a wonderful website. My whole family sat together and selected the card. I got the best price and great quality. Certainly not the best card available but it's value for me.	yes	9
4	SC1233XXP1	2015-12-06 22:12:02.774782+05:30	Paper quality is great.Good buy.	The card is exactly how it looks in the pictures. Barati has been known to provide valuable information. A bit expensive but it's a good buy.	maybe	9
\.


--
-- Name: reviews_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('reviews_id_seq', 4, true);


--
-- Data for Name: social_auth_association; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY social_auth_association (id, server_url, handle, secret, issued, lifetime, assoc_type) FROM stdin;
\.


--
-- Name: social_auth_association_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('social_auth_association_id_seq', 1, false);


--
-- Data for Name: social_auth_code; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY social_auth_code (id, email, code, verified) FROM stdin;
\.


--
-- Name: social_auth_code_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('social_auth_code_id_seq', 1, false);


--
-- Data for Name: social_auth_nonce; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY social_auth_nonce (id, server_url, "timestamp", salt) FROM stdin;
\.


--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('social_auth_nonce_id_seq', 1, false);


--
-- Data for Name: social_auth_usersocialauth; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY social_auth_usersocialauth (id, provider, uid, extra_data, user_id) FROM stdin;
15	facebook	1245708408789585	{"access_token": "CAAYTcrwO38QBAA2bu3uQNqdkdH5jpiiPAUpochMizuptLQgEa8VbCZACbUZBXijpZBIbFig4t3nOqbwfP30g2ZBO0uLLiLTNd10SxmFZCg2YcVUfLoGG4rsGx6u3cDAjmeZCUPzKXOvCbQkBwGrVIHZAJ5eMvLkW47z0qtJhA34Vmj7rQLMh3TUEf8lHZAL2WaFYxLtzHr8ZA2sZCUWKuIdxfx", "expires": null, "id": "1245708408789585"}	28
\.


--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('social_auth_usersocialauth_id_seq', 15, true);


--
-- Data for Name: star_ratings_rating; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY star_ratings_rating (id, count, total, average, object_id, content_type_id) FROM stdin;
2	2	7	3.500	2	30
4	1	4	4.000	2	46
6	0	0	0.000	2	17
5	1	3	3.000	6	30
7	0	0	0.000	1	17
1	3	9	3.000	1	30
3	1	4	4.000	1	46
8	0	0	0.000	11	30
9	0	0	0.000	12	30
10	0	0	0.000	15	17
11	0	0	0.000	8	46
12	0	0	0.000	9	46
\.


--
-- Name: star_ratings_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('star_ratings_rating_id_seq', 12, true);


--
-- Data for Name: star_ratings_userrating; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY star_ratings_userrating (id, created, modified, ip, score, rating_id, user_id) FROM stdin;
1	2015-12-06 10:36:27.526611+05:30	2015-12-06 10:42:11.5732+05:30	127.0.0.1	3	1	12
2	2015-12-06 10:42:31.278097+05:30	2015-12-06 10:43:11.205928+05:30	127.0.0.1	3	2	12
3	2015-12-06 10:47:08.171641+05:30	2015-12-06 10:47:08.171856+05:30	127.0.0.1	2	1	1
4	2015-12-06 10:47:22.906093+05:30	2015-12-06 10:47:22.90631+05:30	127.0.0.1	4	2	1
6	2015-12-12 04:04:09.56762+05:30	2015-12-12 04:04:09.567901+05:30	127.0.0.1	4	4	12
7	2016-01-09 12:05:38.177262+05:30	2016-01-09 12:05:38.177491+05:30	127.0.0.1	3	5	28
5	2015-12-06 20:43:51.013463+05:30	2016-01-10 12:55:44.741679+05:30	127.0.0.1	4	1	28
8	2016-01-10 16:08:00.261118+05:30	2016-01-10 16:08:00.261348+05:30	127.0.0.1	4	3	28
\.


--
-- Name: star_ratings_userrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('star_ratings_userrating_id_seq', 8, true);


--
-- Data for Name: tax_and_refund_policies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tax_and_refund_policies (id, product_type, total_tax, min_payment_needed_before_confirmation, refund_before_confirmation, refund_after_30_days_or_processing, refund_after_die_preparing, refund_between_15_30_days, "timestamp", refund_between_2_7_days, refund_between_7_15_days, refund_within_2_days) FROM stdin;
3	beautician	35	50	100	0	\N	25	2016-01-13 00:05:46.388354+05:30	80	50	100
4	ghodi_bagghi	14.5	50	100	0	\N	25	2016-01-13 00:06:38.958351+05:30	80	50	100
2	card	12.5	100	100	80	50	25	2016-01-12 23:23:57.145355+05:30	80	50	100
5	venue	14.5	50	100	0	\N	25	2016-01-13 21:53:05.902844+05:30	80	50	100
\.


--
-- Name: tax_and_refund_policies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tax_and_refund_policies_id_seq', 5, true);


--
-- Data for Name: tent_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tent_types (id, name) FROM stdin;
\.


--
-- Name: tent_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tent_types_id_seq', 1, false);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users (id, username, first_name, middle_name, last_name, email, contact1, contact2, contact3, address_id, religion_id, role) FROM stdin;
1	abhayg	\N	\N	\N	\N	\N	\N	\N	\N	\N	customer
5	abhay_test@testmail.com	Abhay_test	\N	\N	abhay_test@testmail.com	\N	\N	\N	\N	\N	customer
6	iabhaygupta@yahoo.com	Abhay_test	\N	\N	iabhaygupta@yahoo.com	\N	\N	\N	\N	\N	customer
9	iabhaygupta90@yahoo.com	Abhay	\N	\N	iabhaygupta90@yahoo.com	\N	\N	\N	\N	\N	customer
19	AbhayGupta		\N			\N	\N	\N	\N	\N	customer
10	admin	Abhay		Gupta	iabhaygupta90@gmail.com				\N	\N	admin
21	vendor1		\N			\N	\N	\N	\N	\N	vendor
22	radhikamandapam		\N			\N	\N	\N	\N	\N	vendor
23	shagun		\N			\N	\N	\N	\N	\N	vendor
24	ghanshyam		\N			\N	\N	\N	\N	\N	vendor
25	yoyo		\N			\N	\N	\N	\N	\N	vendor
26	habibs		\N			\N	\N	\N	\N	\N	vendor
27	malhotra		\N			\N	\N	\N	\N	\N	vendor
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('users_id_seq', 27, true);


--
-- Data for Name: vendor_coordinators; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vendor_coordinators (id, coordinator_name, email, contact1, contact2, contact3, vendor_id) FROM stdin;
\.


--
-- Name: vendor_coordinators_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('vendor_coordinators_id_seq', 1, false);


--
-- Data for Name: vendors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vendors (id, name, official_email, contact1, contact2, contact3, address_id, user_id) FROM stdin;
8	Radhika Mandapam					2	22
7	Shagun Marriage Garden					2	23
6	Ghanshyam Tent House					1	24
4	Habibs	habibs@test.com				2	26
1	Malhotra Cards		9110221111			1	27
5	YoYo Tent House					2	25
\.


--
-- Name: vendors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('vendors_id_seq', 8, true);


--
-- Data for Name: venue_types; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY venue_types (id, name) FROM stdin;
1	Indoor
2	Outdoor
3	Covered Outdoor
4	Uncovered
5	Banquet
6	Farm House
7	Historic Place
8	Hotel
\.


--
-- Name: venue_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('venue_types_id_seq', 8, true);


--
-- Data for Name: venues; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY venues (id, ref_id, name, short_description, long_description, max_capacity, accomodation_available, address_id, type_id, vendor_id, actual_price, discount_perc, discount_rs, discounted_price, "timestamp", audio_video_equipment_details, cutlery_and_crockery_details, food_types, function_types, generator_details, rooms_details, number_of_rooms, outside_catering_allowed, outside_decoration_allowed, generator_cost, per_plate_cost_nonveg, per_plate_cost_veg, per_room_per_day_cost, service_staff_details, stage_details, valet_parking, generator_available, generator_cost_type, parking_capacity_2_wheelers, parking_capacity_4_wheelers, wheelchair_accessibility, alcohol_serving) FROM stdin;
1	VN123AQ	Shagun Marriage Garden	Marriage garden for your dream wedding	Marriage garden for your dream wedding	2000	f	2	2	7	25000	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
2	VN2213SW	Radhika Mandapam	Farm House	Perfect Farm House for your dream wedding	1500	t	1	6	8	45000	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
15	VEN_CCVV2	Test marriage garden	test short	test long	2000	t	36	4	1	20000	\N	\N	\N	2016-02-03 12:10:58.827624+05:30	No equipments available	\N	Chinese, Continental, Rajasthani, Punjabi	Marriage, Reception	test generator details	\N	20	t	t	2000	120	99	1000	\N	\N	f	t	excluded	20	50	partially	f
\.


--
-- Name: venues_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('venues_id_seq', 15, true);


--
-- Name: video_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('video_types_id_seq', 4, true);


--
-- Data for Name: videos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY videos (id, ref_id, video_name, video_link, vendor_id_id) FROM stdin;
\.


--
-- Name: videos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('videos_id_seq', 1, false);


--
-- Data for Name: wishlist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY wishlist (id, ref_id, "timestamp", user_id) FROM stdin;
20	HBIS12322XY	2015-12-12 04:04:51.327875+05:30	9
25	HBIS12322XY	2015-12-12 04:21:49.494655+05:30	10
26	TWC123123G1	2015-12-12 04:57:58.498753+05:30	10
38	HBIS12322XX	2016-01-07 10:19:12.970135+05:30	19
39	HBIS12322XY	2016-01-07 10:19:42.730648+05:30	19
41	VN2213SW	2016-01-07 10:19:57.334494+05:30	19
42	SC1233XXP1	2016-01-09 11:42:01.598824+05:30	19
\.


--
-- Name: wishlist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('wishlist_id_seq', 43, true);


--
-- Name: address_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY address
    ADD CONSTRAINT address_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: axes_accessattempt_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY axes_accessattempt
    ADD CONSTRAINT axes_accessattempt_pkey PRIMARY KEY (id);


--
-- Name: axes_accesslog_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY axes_accesslog
    ADD CONSTRAINT axes_accesslog_pkey PRIMARY KEY (id);


--
-- Name: bakery_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY bakery_types
    ADD CONSTRAINT bakery_types_pkey PRIMARY KEY (id);


--
-- Name: band_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY band_types
    ADD CONSTRAINT band_types_pkey PRIMARY KEY (id);


--
-- Name: beautician_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY beautician_types
    ADD CONSTRAINT beautician_types_pkey PRIMARY KEY (id);


--
-- Name: beauticians_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY beauticians
    ADD CONSTRAINT beauticians_pkey PRIMARY KEY (id);


--
-- Name: beauticians_ref_id_17d224881d6f1223_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY beauticians
    ADD CONSTRAINT beauticians_ref_id_17d224881d6f1223_uniq UNIQUE (ref_id);


--
-- Name: budget_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY budget
    ADD CONSTRAINT budget_pkey PRIMARY KEY (id);


--
-- Name: card_colors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY card_colors
    ADD CONSTRAINT card_colors_pkey PRIMARY KEY (id);


--
-- Name: card_deities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY card_deities
    ADD CONSTRAINT card_deities_pkey PRIMARY KEY (id);


--
-- Name: card_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY card_types
    ADD CONSTRAINT card_types_pkey PRIMARY KEY (id);


--
-- Name: cards_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY cards
    ADD CONSTRAINT cards_pkey PRIMARY KEY (id);


--
-- Name: cards_preferences_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY cards_preferences
    ADD CONSTRAINT cards_preferences_pkey PRIMARY KEY (id);


--
-- Name: cards_ref_id_4d6eb9d11fa4c452_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY cards
    ADD CONSTRAINT cards_ref_id_4d6eb9d11fa4c452_uniq UNIQUE (ref_id);


--
-- Name: cart_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY cart
    ADD CONSTRAINT cart_pkey PRIMARY KEY (id);


--
-- Name: delivery_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY delivery_status
    ADD CONSTRAINT delivery_status_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: fireworks_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY fireworks_types
    ADD CONSTRAINT fireworks_types_pkey PRIMARY KEY (id);


--
-- Name: ghodi_bagghi_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ghodi_bagghi_types
    ADD CONSTRAINT ghodi_bagghi_types_pkey PRIMARY KEY (id);


--
-- Name: gift_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY gift_types
    ADD CONSTRAINT gift_types_pkey PRIMARY KEY (id);


--
-- Name: main_preferences_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY main_preferences
    ADD CONSTRAINT main_preferences_pkey PRIMARY KEY (id);


--
-- Name: mehendi_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY mehendi_types
    ADD CONSTRAINT mehendi_types_pkey PRIMARY KEY (id);


--
-- Name: music_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY music_types
    ADD CONSTRAINT music_types_pkey PRIMARY KEY (id);


--
-- Name: orders_package_id_75650ed4f062b8dc_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY orders
    ADD CONSTRAINT orders_package_id_75650ed4f062b8dc_uniq UNIQUE (package_id);


--
-- Name: orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- Name: product_pictures_name_30ab1e9ee7a2c2d1_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY product_pictures
    ADD CONSTRAINT product_pictures_name_30ab1e9ee7a2c2d1_uniq UNIQUE (name);


--
-- Name: product_pictures_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY product_pictures
    ADD CONSTRAINT product_pictures_pkey PRIMARY KEY (id);


--
-- Name: religion_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY religion
    ADD CONSTRAINT religion_name_key UNIQUE (name);


--
-- Name: religion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY religion
    ADD CONSTRAINT religion_pkey PRIMARY KEY (id);


--
-- Name: reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (id);


--
-- Name: social_auth_association_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY social_auth_association
    ADD CONSTRAINT social_auth_association_pkey PRIMARY KEY (id);


--
-- Name: social_auth_code_email_75f27066d057e3b6_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY social_auth_code
    ADD CONSTRAINT social_auth_code_email_75f27066d057e3b6_uniq UNIQUE (email, code);


--
-- Name: social_auth_code_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY social_auth_code
    ADD CONSTRAINT social_auth_code_pkey PRIMARY KEY (id);


--
-- Name: social_auth_nonce_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY social_auth_nonce
    ADD CONSTRAINT social_auth_nonce_pkey PRIMARY KEY (id);


--
-- Name: social_auth_nonce_server_url_36601f978463b4_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY social_auth_nonce
    ADD CONSTRAINT social_auth_nonce_server_url_36601f978463b4_uniq UNIQUE (server_url, "timestamp", salt);


--
-- Name: social_auth_usersocialauth_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersocialauth_pkey PRIMARY KEY (id);


--
-- Name: social_auth_usersocialauth_provider_2f763109e2c4a1fb_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersocialauth_provider_2f763109e2c4a1fb_uniq UNIQUE (provider, uid);


--
-- Name: star_ratings_rating_content_type_id_1fea23398f983929_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY star_ratings_rating
    ADD CONSTRAINT star_ratings_rating_content_type_id_1fea23398f983929_uniq UNIQUE (content_type_id, object_id);


--
-- Name: star_ratings_rating_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY star_ratings_rating
    ADD CONSTRAINT star_ratings_rating_pkey PRIMARY KEY (id);


--
-- Name: star_ratings_userrating_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY star_ratings_userrating
    ADD CONSTRAINT star_ratings_userrating_pkey PRIMARY KEY (id);


--
-- Name: star_ratings_userrating_user_id_5a83a88db79dd2cf_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY star_ratings_userrating
    ADD CONSTRAINT star_ratings_userrating_user_id_5a83a88db79dd2cf_uniq UNIQUE (user_id, rating_id);


--
-- Name: tax_and_refund_policies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tax_and_refund_policies
    ADD CONSTRAINT tax_and_refund_policies_pkey PRIMARY KEY (id);


--
-- Name: tax_and_refund_policies_product_category_49f806ee890ffb7b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tax_and_refund_policies
    ADD CONSTRAINT tax_and_refund_policies_product_category_49f806ee890ffb7b_uniq UNIQUE (product_type);


--
-- Name: tent_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tent_types
    ADD CONSTRAINT tent_types_pkey PRIMARY KEY (id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: vendor_coordinators_coordinator_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vendor_coordinators
    ADD CONSTRAINT vendor_coordinators_coordinator_name_key UNIQUE (coordinator_name);


--
-- Name: vendor_coordinators_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vendor_coordinators
    ADD CONSTRAINT vendor_coordinators_pkey PRIMARY KEY (id);


--
-- Name: vendors_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vendors
    ADD CONSTRAINT vendors_name_key UNIQUE (name);


--
-- Name: vendors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vendors
    ADD CONSTRAINT vendors_pkey PRIMARY KEY (id);


--
-- Name: venue_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY venue_types
    ADD CONSTRAINT venue_types_pkey PRIMARY KEY (id);


--
-- Name: venues_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY venues
    ADD CONSTRAINT venues_pkey PRIMARY KEY (id);


--
-- Name: venues_ref_id_53fb8ff229ca4d2c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY venues
    ADD CONSTRAINT venues_ref_id_53fb8ff229ca4d2c_uniq UNIQUE (ref_id);


--
-- Name: video_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY photo_video_types
    ADD CONSTRAINT video_types_pkey PRIMARY KEY (id);


--
-- Name: videos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY videos
    ADD CONSTRAINT videos_pkey PRIMARY KEY (id);


--
-- Name: wishlist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY wishlist
    ADD CONSTRAINT wishlist_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: beauticians_5b740474; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX beauticians_5b740474 ON beauticians USING btree (vendor_id);


--
-- Name: beauticians_94757cae; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX beauticians_94757cae ON beauticians USING btree (type_id);


--
-- Name: beauticians_ea8e5d12; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX beauticians_ea8e5d12 ON beauticians USING btree (address_id);


--
-- Name: budget_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX budget_e8701ad4 ON budget USING btree (user_id);


--
-- Name: card_colors_dcbdb4d6; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX card_colors_dcbdb4d6 ON card_colors USING btree (card_id);


--
-- Name: card_deities_dcbdb4d6; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX card_deities_dcbdb4d6 ON card_deities USING btree (card_id);


--
-- Name: cards_5b740474; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX cards_5b740474 ON cards USING btree (vendor_id);


--
-- Name: cards_94757cae; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX cards_94757cae ON cards USING btree (type_id);


--
-- Name: cards_ea8e5d12; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX cards_ea8e5d12 ON cards USING btree (address_id);


--
-- Name: cards_preferences_27e65901; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX cards_preferences_27e65901 ON cards_preferences USING btree (card_id);


--
-- Name: cards_preferences_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX cards_preferences_e8701ad4 ON cards_preferences USING btree (user_id);


--
-- Name: cart_18624dd3; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX cart_18624dd3 ON cart USING btree (user_id);


--
-- Name: cart_ref_id_c60d713250ab06c_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX cart_ref_id_c60d713250ab06c_like ON cart USING btree (ref_id varchar_pattern_ops);


--
-- Name: delivery_status_69dfcb07; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX delivery_status_69dfcb07 ON delivery_status USING btree (order_id);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: main_preferences_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX main_preferences_e8701ad4 ON main_preferences USING btree (user_id);


--
-- Name: main_preferences_location_8d9780b70d34788_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX main_preferences_location_8d9780b70d34788_like ON main_preferences USING btree (location varchar_pattern_ops);


--
-- Name: main_preferences_sublocation_302967f58bf50401_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX main_preferences_sublocation_302967f58bf50401_like ON main_preferences USING btree (sublocation varchar_pattern_ops);


--
-- Name: orders_96b1f972; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX orders_96b1f972 ON orders USING btree (vendor_id);


--
-- Name: orders_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX orders_e8701ad4 ON orders USING btree (user_id);


--
-- Name: orders_ea8e5d12; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX orders_ea8e5d12 ON orders USING btree (address_id);


--
-- Name: religion_name_187b864dcbbf0cc1_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX religion_name_187b864dcbbf0cc1_like ON religion USING btree (name varchar_pattern_ops);


--
-- Name: reviews_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX reviews_e8701ad4 ON reviews USING btree (user_id);


--
-- Name: social_auth_code_c1336794; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX social_auth_code_c1336794 ON social_auth_code USING btree (code);


--
-- Name: social_auth_code_code_32d820bdeaa954bc_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX social_auth_code_code_32d820bdeaa954bc_like ON social_auth_code USING btree (code varchar_pattern_ops);


--
-- Name: social_auth_usersocialauth_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX social_auth_usersocialauth_e8701ad4 ON social_auth_usersocialauth USING btree (user_id);


--
-- Name: star_ratings_rating_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX star_ratings_rating_417f1b1c ON star_ratings_rating USING btree (content_type_id);


--
-- Name: star_ratings_userrating_c14e3df7; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX star_ratings_userrating_c14e3df7 ON star_ratings_userrating USING btree (rating_id);


--
-- Name: star_ratings_userrating_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX star_ratings_userrating_e8701ad4 ON star_ratings_userrating USING btree (user_id);


--
-- Name: users_a0b6cc4a; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX users_a0b6cc4a ON users USING btree (religion_id);


--
-- Name: users_ea8e5d12; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX users_ea8e5d12 ON users USING btree (address_id);


--
-- Name: users_username_5c8da42f09dabe4a_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX users_username_5c8da42f09dabe4a_like ON users USING btree (username varchar_pattern_ops);


--
-- Name: vendor_coordinators_5b740474; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vendor_coordinators_5b740474 ON vendor_coordinators USING btree (vendor_id);


--
-- Name: vendor_coordinators_coordinator_name_4501c502ea868f7c_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vendor_coordinators_coordinator_name_4501c502ea868f7c_like ON vendor_coordinators USING btree (coordinator_name varchar_pattern_ops);


--
-- Name: vendors_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vendors_e8701ad4 ON vendors USING btree (user_id);


--
-- Name: vendors_ea8e5d12; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vendors_ea8e5d12 ON vendors USING btree (address_id);


--
-- Name: vendors_name_7522e1c2ededad2a_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vendors_name_7522e1c2ededad2a_like ON vendors USING btree (name varchar_pattern_ops);


--
-- Name: venues_5b740474; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX venues_5b740474 ON venues USING btree (vendor_id);


--
-- Name: venues_94757cae; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX venues_94757cae ON venues USING btree (type_id);


--
-- Name: venues_ea8e5d12; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX venues_ea8e5d12 ON venues USING btree (address_id);


--
-- Name: videos_5b740474; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX videos_5b740474 ON videos USING btree (vendor_id_id);


--
-- Name: wishlist_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX wishlist_e8701ad4 ON wishlist USING btree (user_id);


--
-- Name: new_user_insert; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER new_user_insert AFTER INSERT ON auth_user FOR EACH ROW EXECUTE PROCEDURE insert_new_user_in_users();


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: beauticians_address_id_59ebb9039e6be086_fk_address_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY beauticians
    ADD CONSTRAINT beauticians_address_id_59ebb9039e6be086_fk_address_id FOREIGN KEY (address_id) REFERENCES address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: beauticians_type_id_284a1ffde5f758b_fk_beautician_types_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY beauticians
    ADD CONSTRAINT beauticians_type_id_284a1ffde5f758b_fk_beautician_types_id FOREIGN KEY (type_id) REFERENCES beautician_types(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: beauticians_vendor_id_16859f2aefdc3891_fk_vendors_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY beauticians
    ADD CONSTRAINT beauticians_vendor_id_16859f2aefdc3891_fk_vendors_id FOREIGN KEY (vendor_id) REFERENCES vendors(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: budget_user_id_5ce121a1764e6636_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY budget
    ADD CONSTRAINT budget_user_id_5ce121a1764e6636_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: card_colors_card_id_6f493451434f954a_fk_cards_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY card_colors
    ADD CONSTRAINT card_colors_card_id_6f493451434f954a_fk_cards_id FOREIGN KEY (card_id) REFERENCES cards(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: card_deities_card_id_5550a7e40cc69130_fk_cards_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY card_deities
    ADD CONSTRAINT card_deities_card_id_5550a7e40cc69130_fk_cards_id FOREIGN KEY (card_id) REFERENCES cards(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_address_id_5b9fa788449fb835_fk_address_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cards
    ADD CONSTRAINT cards_address_id_5b9fa788449fb835_fk_address_id FOREIGN KEY (address_id) REFERENCES address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_preferences_card_id_6eeb6691a8f69b8b_fk_cards_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cards_preferences
    ADD CONSTRAINT cards_preferences_card_id_6eeb6691a8f69b8b_fk_cards_id FOREIGN KEY (card_id) REFERENCES cards(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_preferences_user_id_5da8934a577c950_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cards_preferences
    ADD CONSTRAINT cards_preferences_user_id_5da8934a577c950_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_type_id_b4ecf48384987ba_fk_card_types_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cards
    ADD CONSTRAINT cards_type_id_b4ecf48384987ba_fk_card_types_id FOREIGN KEY (type_id) REFERENCES card_types(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_vendor_id_3d1a19adb6f8ac06_fk_vendors_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cards
    ADD CONSTRAINT cards_vendor_id_3d1a19adb6f8ac06_fk_vendors_id FOREIGN KEY (vendor_id) REFERENCES vendors(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cart_user_id_69eda98a9617b929_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cart
    ADD CONSTRAINT cart_user_id_69eda98a9617b929_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: delivery_status_order_id_39d50c0a810d1b1_fk_orders_order_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY delivery_status
    ADD CONSTRAINT delivery_status_order_id_39d50c0a810d1b1_fk_orders_order_id FOREIGN KEY (order_id) REFERENCES orders(order_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_preferences_user_id_29255e6656780b55_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY main_preferences
    ADD CONSTRAINT main_preferences_user_id_29255e6656780b55_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders_address_id_3f8871782af43754_fk_address_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY orders
    ADD CONSTRAINT orders_address_id_3f8871782af43754_fk_address_id FOREIGN KEY (address_id) REFERENCES address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders_user_id_74bfa241d85dd86_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY orders
    ADD CONSTRAINT orders_user_id_74bfa241d85dd86_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders_vendor_id_3c03ee2ae1b3d471_fk_vendors_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY orders
    ADD CONSTRAINT orders_vendor_id_3c03ee2ae1b3d471_fk_vendors_id FOREIGN KEY (vendor_id) REFERENCES vendors(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: reviews_user_id_10d88e91f71cbc39_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reviews
    ADD CONSTRAINT reviews_user_id_10d88e91f71cbc39_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: social_auth_usersocial_user_id_193b2d80880502b2_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersocial_user_id_193b2d80880502b2_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: star_content_type_id_34387b1f1996111a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY star_ratings_rating
    ADD CONSTRAINT star_content_type_id_34387b1f1996111a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: star_ratin_rating_id_1603aaaa4f6f2354_fk_star_ratings_rating_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY star_ratings_userrating
    ADD CONSTRAINT star_ratin_rating_id_1603aaaa4f6f2354_fk_star_ratings_rating_id FOREIGN KEY (rating_id) REFERENCES star_ratings_rating(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: star_ratings_userratin_user_id_709e3d8dec7a0fe8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY star_ratings_userrating
    ADD CONSTRAINT star_ratings_userratin_user_id_709e3d8dec7a0fe8_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_address_id_718d51ced2de8fbc_fk_address_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_address_id_718d51ced2de8fbc_fk_address_id FOREIGN KEY (address_id) REFERENCES address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_religion_id_77f1529f4bc4b446_fk_religion_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_religion_id_77f1529f4bc4b446_fk_religion_id FOREIGN KEY (religion_id) REFERENCES religion(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vendor_coordinators_vendor_id_id_5fdbffaf2b0e7132_fk_vendors_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vendor_coordinators
    ADD CONSTRAINT vendor_coordinators_vendor_id_id_5fdbffaf2b0e7132_fk_vendors_id FOREIGN KEY (vendor_id) REFERENCES vendors(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vendors_address_id_37f874e05b12f99_fk_address_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vendors
    ADD CONSTRAINT vendors_address_id_37f874e05b12f99_fk_address_id FOREIGN KEY (address_id) REFERENCES address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vendors_user_id_7cc6b412b0a12d33_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vendors
    ADD CONSTRAINT vendors_user_id_7cc6b412b0a12d33_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: venues_address_id_5b32e42c699e245b_fk_address_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY venues
    ADD CONSTRAINT venues_address_id_5b32e42c699e245b_fk_address_id FOREIGN KEY (address_id) REFERENCES address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: venues_type_id_39d07de6234dcc6c_fk_venue_types_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY venues
    ADD CONSTRAINT venues_type_id_39d07de6234dcc6c_fk_venue_types_id FOREIGN KEY (type_id) REFERENCES venue_types(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: venues_vendor_id_2db4a27cb4c301a0_fk_vendors_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY venues
    ADD CONSTRAINT venues_vendor_id_2db4a27cb4c301a0_fk_vendors_id FOREIGN KEY (vendor_id) REFERENCES vendors(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: videos_vendor_id_id_6c6e26042dde0fdf_fk_vendors_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY videos
    ADD CONSTRAINT videos_vendor_id_id_6c6e26042dde0fdf_fk_vendors_id FOREIGN KEY (vendor_id_id) REFERENCES vendors(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wishlist_user_id_63bc93783db7b13a_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY wishlist
    ADD CONSTRAINT wishlist_user_id_63bc93783db7b13a_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

