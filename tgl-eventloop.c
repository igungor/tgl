#ifdef EVENT_V2
#include <event2/event.h>
#include <event2/bufferevent.h>
#else
#include <event.h>
#include "event-old.h"
#endif

#include <time.h>

#include "tgl.h"

// based on net_loop function defined at tg/loop.c
void wait_for_event (struct tgl_state *TLS, int flags, int (*is_end)(void)) {
  int last_get_state = time (0);
  while (!is_end || !is_end ()) {

    event_base_loop (TLS->ev_base, EVLOOP_ONCE);

    //if (safe_quit && !TLS->active_queries) {
    /*if (!TLS->active_queries) {*/
      /*printf ("All done. Exit\n");*/
      /*exit (EXIT_SUCCESS);*/
    /*}*/
    if (time (0) - last_get_state > 3600) {
      tgl_do_lookup_state (TLS);
      last_get_state = time (0);
    }

    TLS->serialize_methods->store_state (TLS);
    //update_prompt ();

    /*if (unknown_user_list_pos) {*/
      /*int i;*/
      /*for (i = 0; i < unknown_user_list_pos; i++) {*/
        /*tgl_do_get_user_info (TLS, TGL_MK_USER (unknown_user_list[i]), 0, 0, 0);*/
      /*}*/
      /*unknown_user_list_pos = 0;*/
    /*}*/
  }
}
