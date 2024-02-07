import sqlite3

def create_bd_profil(bd_name):
    conn = sqlite3.connect('database_egg_bot.db')
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS database_{bd_name} (
            agges_index INTEGER,
            win_index INTEGER,
            change_index INTEGER,
            all_ags INTEGER,
            date_of_reg INTEGER
        );
    """)

    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS CHAT (
            id_chat INTEGER
        );
    """)
    conn.commit()
def create_bd_boost(bd_name):
    conn = sqlite3.connect('database_eggBOOST_bot.db')
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS database_{bd_name} (
            cash_index INTEGER,
            proizvod INTEGER,
            vinosliv INTEGER,
            stong INTEGER
        );
    """)
    conn.commit()

def create_bd_boost(bd_name):
    conn = sqlite3.connect('database_achiv_bot.db')
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS database_{bd_name} (
            first_acgiv INTEGER,
            second_achiv INTEGER,
            therd_achiv INTEGER,
            four_achiv INTEGER,
            five_achiv INTEGER,
            sixs_achiv INTEGER,
            sevens_achiv INTEGER,
            eight_achiv INTEGER
        );
    """)
    conn.commit()


def create_bd_admin():
    conn = sqlite3.connect('database_achiv_bot.db')
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS admin_database (
            subscriptio_chanal TEXT,
            chenal_id TEXT,
            sub_user TEXT
        );
    """)
    conn.commit()

