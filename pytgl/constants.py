# *** Do not edit this file ***
# Generated by utils/mkconstants.py

st_init = 0
st_reqpq_sent = 1
st_reqdh_sent = 2
st_client_dh_sent = 3
st_init_temp = 4
st_reqpq_sent_temp = 5
st_reqdh_sent_temp = 6
st_client_dh_sent_temp = 7
st_authorized = 8
st_error = 9

tgl_message_media_none = 0
tgl_message_media_photo = 1
tgl_message_media_video = 2
tgl_message_media_audio = 3
tgl_message_media_document = 4
tgl_message_media_geo = 5
tgl_message_media_contact = 6
tgl_message_media_unsupported = 7
tgl_message_media_photo_encr = 8
tgl_message_media_video_encr = 9
tgl_message_media_audio_encr = 10
tgl_message_media_document_encr = 11

tgl_message_action_none = 0
tgl_message_action_geo_chat_create = 1
tgl_message_action_geo_chat_checkin = 2
tgl_message_action_chat_create = 3
tgl_message_action_chat_edit_title = 4
tgl_message_action_chat_edit_photo = 5
tgl_message_action_chat_delete_photo = 6
tgl_message_action_chat_add_user = 7
tgl_message_action_chat_delete_user = 8
tgl_message_action_set_message_ttl = 9
tgl_message_action_read_messages = 10
tgl_message_action_delete_messages = 11
tgl_message_action_screenshot_messages = 12
tgl_message_action_flush_history = 13
tgl_message_action_resend = 14
tgl_message_action_notify_layer = 15
tgl_message_action_typing = 16
tgl_message_action_noop = 17
tgl_message_action_commit_key = 18
tgl_message_action_abort_key = 19
tgl_message_action_request_key = 20
tgl_message_action_accept_key = 21

tgl_typing_none = 0
tgl_typing_typing = 1
tgl_typing_cancel = 2
tgl_typing_record_video = 3
tgl_typing_upload_video = 4
tgl_typing_record_audio = 5
tgl_typing_upload_audio = 6
tgl_typing_upload_photo = 7
tgl_typing_upload_document = 8
tgl_typing_geo = 9
tgl_typing_choose_contact = 10

sc_none = 0
sc_waiting = 1
sc_request = 2
sc_ok = 3
sc_deleted = 4

tgl_sce_none = 0
tgl_sce_requested = 1
tgl_sce_accepted = 2
tgl_sce_committed = 3

_TGL_HEADERS = r"""
typedef unsigned long size_t;

struct tgl_serialize_callback {
    const char *(*get_auth_key_filename) (void);
    const char *(*get_state_filename) (void);
    const char *(*get_secret_chat_filename) (void);
};

extern struct tgl_serialize_methods tgl_file_methods;

extern struct tgl_net_methods tgl_conn_methods;
void tgln_set_evbase(struct tgl_state *TLS);

extern struct tgl_timer_methods tgl_libevent_timers;

#define FLAG_MESSAGE_EMPTY 1
#define FLAG_DELETED 2
#define FLAG_FORBIDDEN 4
#define FLAG_HAS_PHOTO 8
#define FLAG_CREATED 16
#define FLAG_SESSION_OUTBOUND 32

#define FLAG_USER_SELF 128
#define FLAG_USER_FOREIGN 256
#define FLAG_USER_CONTACT 512
#define FLAG_USER_IN_CONTACT 1024
#define FLAG_USER_OUT_CONTACT 2048

#define FLAG_CHAT_IN_CHAT 128

#define FLAG_ENCRYPTED 4096
#define FLAG_PENDING 8192

typedef struct { int type; int id; } tgl_peer_id_t;

enum tgl_dc_state {
  st_init,
  st_reqpq_sent,
  st_reqdh_sent,
  st_client_dh_sent,
  st_init_temp,
  st_reqpq_sent_temp,
  st_reqdh_sent_temp,
  st_client_dh_sent_temp,
  st_authorized,
  st_error
};

#define MAX_DC_SESSIONS 3

struct tgl_session {
  struct tgl_dc *dc;
  long long session_id;
  long long last_msg_id;
  int seq_no;
  int received_messages;
  struct connection *c;
  struct tree_long *ack_tree;
  struct tgl_timer *ev;
};

struct tgl_dc {
  int id;
  int port;
  int flags;
  enum tgl_dc_state state;
  char *ip;
    struct tgl_session *sessions[MAX_DC_SESSIONS];
  char auth_key[256];
  char temp_auth_key[256];
  char nonce[256];
  char new_nonce[256];
  char server_nonce[256];
  long long auth_key_id;
  long long temp_auth_key_id;

  long long server_salt;
  struct tgl_timer *ev;

  int server_time_delta;
  double server_time_udelta;
  int has_auth;
};

enum tgl_message_media_type {
  tgl_message_media_none,
  tgl_message_media_photo,
  tgl_message_media_video,
  tgl_message_media_audio,
  tgl_message_media_document,
  tgl_message_media_geo,
  tgl_message_media_contact,
  tgl_message_media_unsupported,
  tgl_message_media_photo_encr,
  tgl_message_media_video_encr,
  tgl_message_media_audio_encr,
  tgl_message_media_document_encr,
};

enum tgl_message_action_type {
  tgl_message_action_none,
  tgl_message_action_geo_chat_create,
  tgl_message_action_geo_chat_checkin,
  tgl_message_action_chat_create,
  tgl_message_action_chat_edit_title,
  tgl_message_action_chat_edit_photo,
  tgl_message_action_chat_delete_photo,
  tgl_message_action_chat_add_user,
  tgl_message_action_chat_delete_user,
  tgl_message_action_set_message_ttl,
  tgl_message_action_read_messages,
  tgl_message_action_delete_messages,
  tgl_message_action_screenshot_messages,
  tgl_message_action_flush_history,
  tgl_message_action_resend,
  tgl_message_action_notify_layer,
  tgl_message_action_typing,
  tgl_message_action_noop,
  tgl_message_action_commit_key,
  tgl_message_action_abort_key,
  tgl_message_action_request_key,
  tgl_message_action_accept_key
};

enum tgl_typing_status {
  tgl_typing_none,
  tgl_typing_typing,
  tgl_typing_cancel,
  tgl_typing_record_video,
  tgl_typing_upload_video,
  tgl_typing_record_audio,
  tgl_typing_upload_audio,
  tgl_typing_upload_photo,
  tgl_typing_upload_document,
  tgl_typing_geo,
  tgl_typing_choose_contact
};

struct tgl_file_location {
  int dc;
  long long volume;
  int local_id;
  long long secret;
};

struct tgl_photo_size {
  char *type;
  struct tgl_file_location loc;
  int w;
  int h;
  int size;
  char *data;
};

struct tgl_geo {
  double longitude;
  double latitude;
};

struct tgl_photo {
  long long id;
  long long access_hash;
  int user_id;
  int date;
  char *caption;
  struct tgl_geo geo;
  int sizes_num;
  struct tgl_photo_size *sizes;
};

struct tgl_encr_photo {
  long long id;
  long long access_hash;
  int dc_id;
  int size;
  int key_fingerprint;

  unsigned char *key;
  unsigned char *iv;
  int w;
  int h;
};

struct tgl_encr_video {
  long long id;
  long long access_hash;
  int dc_id;
  int size;
  int key_fingerprint;
  
  unsigned char *key;
  unsigned char *iv;
  int w;
  int h;
  int duration;
  char *mime_type;
};

struct tgl_encr_audio {
  long long id;
  long long access_hash;
  int dc_id;
  int size;
  int key_fingerprint;
  
  unsigned char *key;
  unsigned char *iv;
  int duration;
  char *mime_type;
};

struct tgl_encr_document {
  long long id;
  long long access_hash;
  int dc_id;
  int size;
  int key_fingerprint;
  
  unsigned char *key;
  unsigned char *iv;
  char *file_name;
  char *mime_type;
};

struct tgl_encr_file {
  char *filename;
  unsigned char *key;
  unsigned char *iv;
};

struct tgl_user_status {
  int online;
  int when;
  struct tgl_timer *ev;
};

struct tgl_user {
  tgl_peer_id_t id;
  int flags;
  struct tgl_message *last;
  char *print_name;
  int structure_version;
  struct tgl_file_location photo_big;
  struct tgl_file_location photo_small;
  long long photo_id;
  struct tgl_photo photo;
  char *first_name;
  char *last_name;
  char *phone;
  long long access_hash;
  struct tgl_user_status status;
  int blocked;
  char *real_first_name;
  char *real_last_name;
  char *username;
};

struct tgl_chat_user {
  int user_id;
  int inviter_id;
  int date;
};

struct tgl_chat {
  tgl_peer_id_t id;
  int flags;
  struct tgl_message *last;
  char *print_title;
  int structure_version;
  struct tgl_file_location photo_big;
  struct tgl_file_location photo_small;
  struct tgl_photo photo;
  char *title;
  int users_num;
  int user_list_size;
  int user_list_version;
  struct tgl_chat_user *user_list;
  int date;
  int version;
  int admin_id;
};

enum tgl_secret_chat_state {
  sc_none,
  sc_waiting,
  sc_request,
  sc_ok,
  sc_deleted
};

enum tgl_secret_chat_exchange_state {
  tgl_sce_none,
  tgl_sce_requested,
  tgl_sce_accepted,
  tgl_sce_committed
};

struct tgl_secret_chat {
  tgl_peer_id_t id;
  int flags;
  struct tgl_message *last;
  char *print_name;
  int structure_version;
  struct tgl_file_location photo_big;
  struct tgl_file_location photo_small;
  struct tgl_photo photo;
  int user_id;
  int admin_id;
  int date;
  int ttl;
  int layer;
  int in_seq_no;
  int out_seq_no;
  int last_in_seq_no;
  long long access_hash;
  unsigned char *g_key;
  unsigned char *nonce;

  enum tgl_secret_chat_state state;
  int key[64];
  long long key_fingerprint;
  unsigned char first_key_sha[20];

  long long exchange_id;
  enum tgl_secret_chat_exchange_state exchange_state;
  int exchange_key[64];
  long long exchange_key_fingerprint;
};

typedef union tgl_peer {
  struct {
    tgl_peer_id_t id;
    int flags;
    struct tgl_message *last;
    char *print_name;
    int structure_version;
    struct tgl_file_location photo_big;
    struct tgl_file_location photo_small;
    struct tgl_photo photo;
  };
  struct tgl_user user;
  struct tgl_chat chat;
  struct tgl_secret_chat encr_chat;
} tgl_peer_t;

struct tgl_video {
  long long id;
  long long access_hash;
  int user_id;
  int date;
  int size;
  int dc_id;
  struct tgl_photo_size thumb;
  char *caption;
  int duration;
  int w;
  int h;
  char *mime_type;
};

struct tgl_audio {
  long long id;
  long long access_hash;
  int user_id;
  int date;
  int size;
  int dc_id;
  int duration;
  char *mime_type;
};

struct tgl_document {
  long long id;
  long long access_hash;
  int user_id;
  int date;
  int size;
  int dc_id;
  struct tgl_photo_size thumb;
  char *caption;
  char *mime_type;
};

struct tgl_message_action {
  enum tgl_message_action_type type;
  union {
    struct {
      char *title;
      int user_num;
      int *users;
    };
    char *new_title;
    struct tgl_photo photo;
    int user;
    int ttl;
    int layer;
    int read_cnt;
    int delete_cnt;
    int screenshot_cnt;
    enum tgl_typing_status typing;
    struct {
      int start_seq_no;
      int end_seq_no;
    };
    struct {
      unsigned char *g_a;
      long long exchange_id;
      long long key_fingerprint;
    };
  };
};

struct tgl_message_media {
  enum tgl_message_media_type type;
  union {
    struct tgl_photo photo;
    struct tgl_video video;
    struct tgl_audio audio;
    struct tgl_document document;
    struct tgl_geo geo;
    struct {
      char *phone;
      char *first_name;
      char *last_name;
      int user_id;
    };
    struct tgl_encr_photo encr_photo;
    struct tgl_encr_video encr_video;
    struct tgl_encr_audio encr_audio;
    struct tgl_encr_document encr_document;
    struct tgl_encr_file encr_file;
    struct {
      void *data;
      int data_size;
    };
  };
};

struct tgl_message {
  struct tgl_message *next_use, *prev_use;
  struct tgl_message *next, *prev;
  long long id;
  int flags;
  tgl_peer_id_t fwd_from_id;
  int fwd_date;
  tgl_peer_id_t from_id;
  tgl_peer_id_t to_id;
  int out;
  int unread;
  int date;
  int service;
  union {
    struct tgl_message_action action;
    struct {
      char *message;
      int message_len;
      struct tgl_message_media media;
    };
  };
};

void bl_do_set_auth_key_id (struct tgl_state *TLS, int num, unsigned char *buf);

void bl_do_dc_option (struct tgl_state *TLS, int id, int l1, const char *name, int l2, const char *ip, int port);

void bl_do_set_our_id (struct tgl_state *TLS, int id);
void bl_do_user_add (struct tgl_state *TLS, int id, const char *f, int fl, const char *l, int ll, long long access_token, const char *p, int pl, int contact);
void bl_do_user_delete (struct tgl_state *TLS, struct tgl_user *U);
void bl_do_set_user_profile_photo (struct tgl_state *TLS, struct tgl_user *U, long long photo_id, struct tgl_file_location *big, struct tgl_file_location *small);
void bl_do_user_set_name (struct tgl_state *TLS, struct tgl_user *U, const char *f, int fl, const char *l, int ll);
void bl_do_user_set_username (struct tgl_state *TLS, struct tgl_user *U, const char *f, int l);
void bl_do_user_set_access_hash (struct tgl_state *TLS, struct tgl_user *U, long long access_token);
void bl_do_user_set_phone (struct tgl_state *TLS, struct tgl_user *U, const char *p, int pl);
void bl_do_user_set_friend (struct tgl_state *TLS, struct tgl_user *U, int friend);
void bl_do_user_set_full_photo (struct tgl_state *TLS, struct tgl_user *U, const int *start, int len);
void bl_do_user_set_blocked (struct tgl_state *TLS, struct tgl_user *U, int blocked);
void bl_do_user_set_real_name (struct tgl_state *TLS, struct tgl_user *U, const char *f, int fl, const char *l, int ll);

void bl_do_encr_chat_delete (struct tgl_state *TLS, struct tgl_secret_chat *U);
void bl_do_encr_chat_requested (struct tgl_state *TLS, struct tgl_secret_chat *U, long long access_hash, int date, int admin_id, int user_id, unsigned char g_key[], unsigned char nonce[]);
void bl_do_encr_chat_create (struct tgl_state *TLS, int id, int user_id, int admin_id, char *name, int name_len);
void bl_do_encr_chat_set_access_hash (struct tgl_state *TLS, struct tgl_secret_chat *U, long long access_hash);
void bl_do_encr_chat_set_date (struct tgl_state *TLS, struct tgl_secret_chat *U, int date);
void bl_do_encr_chat_set_state (struct tgl_state *TLS, struct tgl_secret_chat *U, enum tgl_secret_chat_state state);
void bl_do_encr_chat_set_ttl (struct tgl_state *TLS, struct tgl_secret_chat *U, int ttl);
void bl_do_encr_chat_set_layer (struct tgl_state *TLS, struct tgl_secret_chat *U, int layer);
void bl_do_encr_chat_accepted (struct tgl_state *TLS, struct tgl_secret_chat *U, const unsigned char g_key[], const unsigned char nonce[], long long key_fingerprint);
void bl_do_encr_chat_set_key (struct tgl_state *TLS, struct tgl_secret_chat *E, unsigned char key[], long long key_fingerprint);
void bl_do_encr_chat_set_sha (struct tgl_state *TLS, struct tgl_secret_chat *E, unsigned char sha[]);
void bl_do_encr_chat_init (struct tgl_state *TLS, int id, int user_id, unsigned char random[], unsigned char g_a[]);
void bl_do_encr_chat_update_seq (struct tgl_state *TLS, struct tgl_secret_chat *E, int in_seq_no, int out_seq_no);
void bl_do_encr_chat_set_seq (struct tgl_state *TLS, struct tgl_secret_chat *E, int in_seq_no, int last_in_seq_no, int out_seq_no);
void bl_do_encr_chat_exchange_request (struct tgl_state *TLS, struct tgl_secret_chat *E, long long id, unsigned char a[]);
void bl_do_encr_chat_exchange_accept (struct tgl_state *TLS, struct tgl_secret_chat *E, long long id, unsigned char key[]);
void bl_do_encr_chat_exchange_commit (struct tgl_state *TLS, struct tgl_secret_chat *E, unsigned char key[]);
void bl_do_encr_chat_exchange_confirm (struct tgl_state *TLS, struct tgl_secret_chat *E);
void bl_do_encr_chat_exchange_abort (struct tgl_state *TLS, struct tgl_secret_chat *E);

void bl_do_dc_signed (struct tgl_state *TLS, int id);
void bl_do_set_working_dc (struct tgl_state *TLS, int num);
void bl_do_set_dh_params (struct tgl_state *TLS, int root, unsigned char prime[], int version);

void bl_do_set_pts (struct tgl_state *TLS, int pts);
void bl_do_set_qts (struct tgl_state *TLS, int qts);
void bl_do_set_seq (struct tgl_state *TLS, int seq);
void bl_do_set_date (struct tgl_state *TLS, int date);

void bl_do_create_chat (struct tgl_state *TLS, struct tgl_chat *C, int y, const char *s, int l, int users_num, int date, int version, struct tgl_file_location *big, struct tgl_file_location *small);
void bl_do_chat_forbid (struct tgl_state *TLS, struct tgl_chat *C, int on);
void bl_do_chat_set_title (struct tgl_state *TLS, struct tgl_chat *C, const char *s, int l);
void bl_do_chat_set_photo (struct tgl_state *TLS, struct tgl_chat *C, struct tgl_file_location *big, struct tgl_file_location *small);
void bl_do_chat_set_date (struct tgl_state *TLS, struct tgl_chat *C, int date);
void bl_do_chat_set_set_in_chat (struct tgl_state *TLS, struct tgl_chat *C, int on);
void bl_do_chat_set_version (struct tgl_state *TLS, struct tgl_chat *C, int version, int user_num);
void bl_do_chat_set_admin (struct tgl_state *TLS, struct tgl_chat *C, int admin);
void bl_do_chat_set_participants (struct tgl_state *TLS, struct tgl_chat *C, int version, int user_num, struct tgl_chat_user *users);
void bl_do_chat_set_full_photo (struct tgl_state *TLS, struct tgl_chat *U, const int *start, int len);
void bl_do_chat_add_user (struct tgl_state *TLS, struct tgl_chat *C, int version, int user, int inviter, int date);
void bl_do_chat_del_user (struct tgl_state *TLS, struct tgl_chat *C, int version, int user);

void bl_do_create_message_text (struct tgl_state *TLS, int msg_id, int from_id, int to_type, int to_id, int date, int unread, int l, const char *s);
void bl_do_create_message_text_fwd (struct tgl_state *TLS, int msg_id, int from_id, int to_type, int to_id, int date, int fwd, int fwd_date, int unread, int l, const char *s);
void bl_do_create_message_service (struct tgl_state *TLS, int msg_id, int from_id, int to_type, int to_id, int date, int unread, const int *data, int len);
void bl_do_create_message_service_fwd (struct tgl_state *TLS, int msg_id, int from_id, int to_type, int to_id, int date, int fwd, int fwd_date, int unread, const int *data, int len);
void bl_do_create_message_media (struct tgl_state *TLS, int msg_id, int from_id, int to_type, int to_id, int date, int unread, int l, const char *s, const int *data, int len);
void bl_do_create_message_media_encr_pending (struct tgl_state *TLS, long long msg_id, int from_id, int to_type, int to_id, int date, int l, const char *s, const int *data, int len);
void bl_do_create_message_media_encr_sent (struct tgl_state *TLS, long long msg_id, const int *data, int len);
void bl_do_create_message_media_fwd (struct tgl_state *TLS, int msg_id, int from_id, int to_type, int to_id, int date, int fwd, int fwd_date, int unread, int l, const char *s, const int *data, int len);
void bl_do_create_message_media_encr (struct tgl_state *TLS, long long msg_id, int from_id, int to_type, int to_id, int date, int l, const char *s, const int *data, int len, const int *data2, int len2);
void bl_do_create_message_service_encr (struct tgl_state *TLS, long long msg_id, int from_id, int to_type, int to_id, int date, const int *data, int len);
void bl_do_send_message_text (struct tgl_state *TLS, long long msg_id, int from_id, int to_type, int to_id, int date, int l, const char *s);
void bl_do_send_message_action_encr (struct tgl_state *TLS, long long msg_id, int from_id, int to_type, int to_id, int date, int l, const int *s);
void bl_do_set_unread (struct tgl_state *TLS, struct tgl_message *M, int unread);
void bl_do_set_message_sent (struct tgl_state *TLS, struct tgl_message *M);
void bl_do_set_msg_id (struct tgl_state *TLS, struct tgl_message *M, int id);
void bl_do_msg_set_outbound (struct tgl_state *TLS, long long id);
void bl_do_delete_msg (struct tgl_state *TLS, struct tgl_message *M);

void bl_do_msg_seq_update (struct tgl_state *TLS, long long id);
void bl_do_msg_update (struct tgl_state *TLS, long long id);
void bl_do_msg_set_oubound (struct tgl_state *TLS, long long id);

void bl_do_reset_authorization (struct tgl_state *TLS);

void wait_for_event (struct tgl_state *TLS, int flags, int (*is_end)(void));

#define TGL_MAX_DC_NUM 100
#define TG_SERVER_DEFAULT 4
#define TG_SERVER_TEST_DEFAULT 2

#define TGL_ENCRYPTED_LAYER 17
#define TGL_SCHEME_LAYER 19

struct connection;
struct mtproto_methods;
struct tgl_session;
struct tgl_dc;

#define TGL_UPDATE_CREATED 1
#define TGL_UPDATE_DELETED 2
#define TGL_UPDATE_PHONE 4
#define TGL_UPDATE_CONTACT 8
#define TGL_UPDATE_PHOTO 16
#define TGL_UPDATE_BLOCKED 32
#define TGL_UPDATE_REAL_NAME 64
#define TGL_UPDATE_NAME 128
#define TGL_UPDATE_REQUESTED 256
#define TGL_UPDATE_WORKING 512
#define TGL_UPDATE_FLAGS 1024
#define TGL_UPDATE_TITLE 2048
#define TGL_UPDATE_ADMIN 4096
#define TGL_UPDATE_MEMBERS 8192
#define TGL_UPDATE_ACCESS_HASH 16384

struct tgl_allocator {
  void *(*alloc)(size_t size);
  void *(*realloc)(void *ptr, size_t old_size, size_t size);
  void (*free)(void *ptr, int size);
  void (*check)(void);
  void (*exists)(void *ptr, int size);
};
extern struct tgl_allocator tgl_allocator_release;
extern struct tgl_allocator tgl_allocator_debug;
struct tgl_state;

struct tgl_update_callback {
  void (*new_msg)(struct tgl_state *TLS, struct tgl_message *M);
  void (*marked_read)(struct tgl_state *TLS, int num, struct tgl_message *list[]);
  int (*logprintf)(const char *format, ...);

  void (*type_notification)(struct tgl_state *TLS, struct tgl_user *U, enum tgl_typing_status status);
  void (*type_in_chat_notification)(struct tgl_state *TLS, struct tgl_user *U, struct tgl_chat *C, enum tgl_typing_status status);
  void (*type_in_secret_chat_notification)(struct tgl_state *TLS, struct tgl_secret_chat *E);
  void (*status_notification)(struct tgl_state *TLS, struct tgl_user *U);
  void (*user_registered)(struct tgl_state *TLS, struct tgl_user *U);
  void (*user_activated)(struct tgl_state *TLS, struct tgl_user *U);
  void (*new_authorization)(struct tgl_state *TLS, const char *device, const char *location);
  void (*chat_update)(struct tgl_state *TLS, struct tgl_chat *C, unsigned flags);
  void (*user_update)(struct tgl_state *TLS, struct tgl_user *C, unsigned flags);
  void (*secret_chat_update)(struct tgl_state *TLS, struct tgl_secret_chat *C, unsigned flags);
  void (*msg_receive)(struct tgl_state *TLS, struct tgl_message *M);
  void (*our_id)(struct tgl_state *TLS, int id);
  void (*notification)(struct tgl_state *TLS, char *type, char *message);
  void (*user_status_update)(struct tgl_state *TLS, struct tgl_user *U);
  char *(*create_print_name) (struct tgl_state *TLS, tgl_peer_id_t id, const char *a1, const char *a2, const char *a3, const char *a4);
};

struct tgl_net_methods {
  int (*write_out) (struct connection *c, const void *data, int len);
  int (*read_in) (struct connection *c, void *data, int len);
  int (*read_in_lookup) (struct connection *c, void *data, int len);
  void (*flush_out) (struct connection *c);
  void (*incr_out_packet_num) (struct connection *c);
  void (*free) (struct connection *c);
  struct tgl_dc *(*get_dc) (struct connection *c);
  struct tgl_session *(*get_session) (struct connection *c);

  struct connection *(*create_connection) (struct tgl_state *TLS, const char *host, int port, struct tgl_session *session, struct tgl_dc *dc, struct mtproto_methods *methods);
};

struct tgl_serialize_methods {
    int (*load_auth) (struct tgl_state *TLS);
    int (*load_state) (struct tgl_state *TLS);
    int (*load_secret_chats) (struct tgl_state *TLS);
    int (*store_auth) (struct tgl_state *TLS);
    int (*store_state) (struct tgl_state *TLS);
    int (*store_secret_chats) (struct tgl_state *TLS);
};

struct mtproto_methods {
  int (*ready) (struct tgl_state *TLS, struct connection *c);
  int (*close) (struct tgl_state *TLS, struct connection *c);
  int (*execute) (struct tgl_state *TLS, struct connection *c, int op, int len);
};

struct tgl_timer;

struct tgl_timer_methods {
  struct tgl_timer *(*alloc) (struct tgl_state *TLS, void (*cb)(struct tgl_state *TLS, void *arg), void *arg);
  void (*insert) (struct tgl_timer *t, double timeout);
  void (*remove) (struct tgl_timer *t);
  void (*free) (struct tgl_timer *t);
};

#define E_ERROR 0
#define E_WARNING 1
#define E_NOTICE 2
#define E_DEBUG 6

#define TGL_LOCK_DIFF 1

#define TGL_MAX_RSA_KEYS_NUM 10

struct tgl_state {
  int our_id;   int encr_root;
  unsigned char *encr_prime;
  int encr_param_version;
  int pts;
  int qts;
  int date;
  int seq;
  int binlog_enabled;
  int test_mode; 
  int verbosity;
  int unread_messages;
  int active_queries;
  int max_msg_id;
  int started;

  long long locks; 
  struct tgl_dc *DC_list[TGL_MAX_DC_NUM];
  struct tgl_dc *DC_working;
  int max_dc_num;
  int dc_working_num;
  int enable_pfs;
  int temp_key_expire_time;

  long long cur_uploading_bytes;
  long long cur_uploaded_bytes;
  long long cur_downloading_bytes;
  long long cur_downloaded_bytes;

  char *binlog_name;
  char *auth_file;
  char *state_file;
  char *secret_chat_file;
  char *downloads_directory;

  struct tgl_update_callback callback;
  struct tgl_net_methods *net_methods;
  struct tgl_serialize_methods *serialize_methods;
  void *ev_base;

  char *rsa_key_list[TGL_MAX_RSA_KEYS_NUM];
  int rsa_key_num;
  struct bignum_ctx *BN_ctx;

  struct tgl_allocator allocator;

  struct tree_peer *peer_tree;
  struct tree_peer_by_name *peer_by_name_tree;
  struct tree_message *message_tree;
  struct tree_message *message_unsent_tree;

  int users_allocated;
  int chats_allocated;
  int messages_allocated;
  int peer_num;
  int peer_size;
  int encr_chats_allocated;
  int geo_chats_allocated;

  tgl_peer_t **Peers;
  struct tgl_message message_list;

  int binlog_fd;

  struct tgl_timer_methods *timer_methods;

  void *pubKey;

  struct tree_query *queries_tree;

  char *base_path; 
  
  struct tree_user *online_updates;

  struct tgl_timer *online_updates_timer;

  int app_id;
  char *app_hash;
};

void tgl_reopen_binlog_for_writing (struct tgl_state *TLS);
void tgl_replay_log (struct tgl_state *TLS);

int tgl_print_stat (struct tgl_state *TLS, char *s, int len);
tgl_peer_t *tgl_peer_get (struct tgl_state *TLS, tgl_peer_id_t id);
tgl_peer_t *tgl_peer_get_by_name (struct tgl_state *TLS, const char *s);

struct tgl_message *tgl_message_get (struct tgl_state *TLS, long long id);
void tgl_peer_iterator_ex (struct tgl_state *TLS, void (*it)(tgl_peer_t *P, void *extra), void *extra);

int tgl_complete_user_list (struct tgl_state *TLS, int index, const char *text, int len, char **R);
int tgl_complete_chat_list (struct tgl_state *TLS, int index, const char *text, int len, char **R);
int tgl_complete_encr_chat_list (struct tgl_state *TLS, int index, const char *text, int len, char **R);
int tgl_complete_peer_list (struct tgl_state *TLS, int index, const char *text, int len, char **R);
int tgl_secret_chat_for_user (struct tgl_state *TLS, tgl_peer_id_t user_id);

#define TGL_PEER_USER 1
#define TGL_PEER_CHAT 2
#define TGL_PEER_GEO_CHAT 3
#define TGL_PEER_ENCR_CHAT 4
#define TGL_PEER_UNKNOWN 0

void tgl_set_binlog_mode (struct tgl_state *TLS, int mode);
void tgl_set_binlog_path (struct tgl_state *TLS, const char *path);
void tgl_set_auth_file_path (struct tgl_state *TLS, const char *path);
void tgl_set_state_file_path (struct tgl_state *TLS, const char *path);
void tgl_set_secret_chat_file_path (struct tgl_state *TLS, const char *path);
void tgl_set_download_directory (struct tgl_state *TLS, const char *path);
void tgl_set_callback (struct tgl_state *TLS, struct tgl_update_callback *cb);
void tgl_set_rsa_key (struct tgl_state *TLS, const char *key);
void tgl_do_help_get_config (struct tgl_state *TLS, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_send_code (struct tgl_state *TLS, const char *user, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, int registered, const char *hash), void *callback_extra);
void tgl_do_phone_call (struct tgl_state *TLS, const char *user, const char *hash, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
int tgl_do_send_code_result (struct tgl_state *TLS, const char *user, const char *hash, const char *code, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_user *Self), void *callback_extra) ;
int tgl_do_send_code_result_auth (struct tgl_state *TLS, const char *user, const char *hash, const char *code, const char *first_name, const char *last_name, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_user *Self), void *callback_extra);
void tgl_do_update_contact_list (struct tgl_state *TLS, void (*callback) (struct tgl_state *TLS, void *callback_extra, int success, int size, struct tgl_user *contacts[]), void *callback_extra);
void tgl_do_send_message (struct tgl_state *TLS, tgl_peer_id_t id, const char *msg, int len, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_send_msg (struct tgl_state *TLS, struct tgl_message *M, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_send_text (struct tgl_state *TLS, tgl_peer_id_t id, char *file, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_mark_read (struct tgl_state *TLS, tgl_peer_id_t id, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_get_history (struct tgl_state *TLS, tgl_peer_id_t id, int limit, int offline_mode, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, int size, struct tgl_message *list[]), void *callback_extra);
void tgl_do_get_history_ext (struct tgl_state *TLS, tgl_peer_id_t id, int offset, int limit, int offline_mode, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, int size, struct tgl_message *list[]), void *callback_extra);
void tgl_do_get_dialog_list (struct tgl_state *TLS, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, int size, tgl_peer_id_t peers[], int last_msg_id[], int unread_count[]), void *callback_extra);
void tgl_do_send_photo (struct tgl_state *TLS, enum tgl_message_media_type type, tgl_peer_id_t to_id, char *file_name, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_set_chat_photo (struct tgl_state *TLS, tgl_peer_id_t chat_id, char *file_name, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_set_profile_photo (struct tgl_state *TLS, char *file_name, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_set_profile_name (struct tgl_state *TLS, char *first_name, char *last_name, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_user *U), void *callback_extra);
void tgl_do_set_username (struct tgl_state *TLS, char *name, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_user *U), void *callback_extra);
void tgl_do_forward_message (struct tgl_state *TLS, tgl_peer_id_t id, int n, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_rename_chat (struct tgl_state *TLS, tgl_peer_id_t id, char *name, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_get_chat_info (struct tgl_state *TLS, tgl_peer_id_t id, int offline_mode, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_chat *C), void *callback_extra);
void tgl_do_get_user_info (struct tgl_state *TLS, tgl_peer_id_t id, int offline_mode, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_user *U), void *callback_extra);
void tgl_do_load_photo (struct tgl_state *TLS, struct tgl_photo *photo, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, char *filename), void *callback_extra);
void tgl_do_load_video_thumb (struct tgl_state *TLS, struct tgl_video *video, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, char *filename), void *callback_extra);
void tgl_do_load_audio (struct tgl_state *TLS, struct tgl_audio *V, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, char *filename), void *callback_extra);
void tgl_do_load_video (struct tgl_state *TLS, struct tgl_video *V, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, char *filename), void *callback_extra);
void tgl_do_load_document (struct tgl_state *TLS, struct tgl_document *V, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, char *filename), void *callback_extra);
void tgl_do_load_document_thumb (struct tgl_state *TLS, struct tgl_document *video, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, char *filename), void *callback_extra);
void tgl_do_load_encr_video (struct tgl_state *TLS, struct tgl_encr_video *V, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, char *filename), void *callback_extra);
void tgl_do_export_auth (struct tgl_state *TLS, int num, void (*callback) (struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_add_contact (struct tgl_state *TLS, const char *phone, int phone_len, const char *first_name, int first_name_len, const char *last_name, int last_name_len, int force, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, int size, struct tgl_user *users[]), void *callback_extra);
void tgl_do_msg_search (struct tgl_state *TLS, tgl_peer_id_t id, int from, int to, int limit, int offset, const char *s, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, int size, struct tgl_message *list[]), void *callback_extra);
void tgl_do_create_encr_chat_request (struct tgl_state *TLS, int user_id, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_secret_chat *E), void *callback_extra);
void tgl_do_create_secret_chat (struct tgl_state *TLS, tgl_peer_id_t id, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_secret_chat *E), void *callback_extra);
void tgl_do_accept_encr_chat_request (struct tgl_state *TLS, struct tgl_secret_chat *E, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_secret_chat *E), void *callback_extra);
void tgl_do_get_difference (struct tgl_state *TLS, int sync_from_start, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_lookup_state (struct tgl_state *TLS);
void tgl_do_add_user_to_chat (struct tgl_state *TLS, tgl_peer_id_t chat_id, tgl_peer_id_t id, int limit, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_del_user_from_chat (struct tgl_state *TLS, tgl_peer_id_t chat_id, tgl_peer_id_t id, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_create_group_chat (struct tgl_state *TLS, tgl_peer_id_t id, char *chat_topic, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_create_group_chat_ex (struct tgl_state *TLS, int users_num, tgl_peer_id_t ids[], char *chat_topic, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_delete_msg (struct tgl_state *TLS, long long id, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_restore_msg (struct tgl_state *TLS, long long id, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_update_status (struct tgl_state *TLS, int online, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_help_get_config_dc (struct tgl_state *TLS, struct tgl_dc *D, void (*callback)(struct tgl_state *TLS, void *, int), void *callback_extra);
void tgl_do_export_card (struct tgl_state *TLS, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, int size, int *card), void *callback_extra);
void tgl_do_import_card (struct tgl_state *TLS, int size, int *card, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_user *U), void *callback_extra);
void tgl_do_send_contact (struct tgl_state *TLS, tgl_peer_id_t id, const char *phone, int phone_len, const char *first_name, int first_name_len, const char *last_name, int last_name_len, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_forward_media (struct tgl_state *TLS, tgl_peer_id_t id, int n, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_del_contact (struct tgl_state *TLS, tgl_peer_id_t id, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_set_encr_chat_ttl (struct tgl_state *TLS, struct tgl_secret_chat *E, int ttl, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_send_location (struct tgl_state *TLS, tgl_peer_id_t id, double latitude, double longitude, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, struct tgl_message *M), void *callback_extra);
void tgl_do_contact_search (struct tgl_state *TLS, char *name, int limit, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, int cnt, struct tgl_user *U[]), void *callback_extra);
void tgl_do_request_exchange (struct tgl_state *TLS, struct tgl_secret_chat *E);
void tgl_do_send_typing (struct tgl_state *TLS, tgl_peer_id_t id, enum tgl_typing_status status, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success), void *callback_extra);
void tgl_do_send_broadcast (struct tgl_state *TLS, int num, tgl_peer_id_t id[], const char *text, int text_len, void (*callback)(struct tgl_state *TLS, void *extra, int success, int num, struct tgl_message *ML[]), void *callback_extra);

void tgl_do_visualize_key (struct tgl_state *TLS, tgl_peer_id_t id, unsigned char buf[16]);

void tgl_do_send_ping (struct tgl_state *TLS, struct connection *c);

void tgl_do_send_extf (struct tgl_state *TLS, char *data, int data_len, void (*callback)(struct tgl_state *TLS, void *callback_extra, int success, char *data), void *callback_extra);

int tgl_authorized_dc (struct tgl_state *TLS, struct tgl_dc *DC);
int tgl_signed_dc (struct tgl_state *TLS, struct tgl_dc *DC);

void tgl_do_create_keys_end (struct tgl_state *TLS, struct tgl_secret_chat *U);
void tgl_do_send_encr_chat_layer (struct tgl_state *TLS, struct tgl_secret_chat *E);

void tgl_init (struct tgl_state *TLS);
void tgl_dc_authorize (struct tgl_state *TLS, struct tgl_dc *DC);

void tgl_dc_iterator (struct tgl_state *TLS, void (*iterator)(struct tgl_dc *DC));
void tgl_dc_iterator_ex (struct tgl_state *TLS, void (*iterator)(struct tgl_dc *DC, void *extra), void *extra);

double tglt_get_double_time (void);

void tgl_insert_empty_user (struct tgl_state *TLS, int id);
void tgl_insert_empty_chat (struct tgl_state *TLS, int id);

int tglf_extf_autocomplete (struct tgl_state *TLS, const char *text, int text_len, int index, char **R, char *data, int data_len);
struct paramed_type *tglf_extf_store (struct tgl_state *TLS, const char *data, int data_len);
char *tglf_extf_fetch (struct tgl_state *TLS, struct paramed_type *T);

void tgl_free_all (struct tgl_state *TLS);
void tgl_register_app_id (struct tgl_state *TLS, int app_id, char *app_hash);

"""
