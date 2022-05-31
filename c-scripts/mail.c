#include "./lib/iniparser/iniparser.h"
#include "./lib/smtp/smtp.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct setting {
  char* port;
  char* server;
  int connection_security;
  enum smtp_flag mail_flag;
  enum smtp_authentication_method auth;
  char* user;
  char* pass;
} m_setting;

typedef struct body {
  char* from;
  char* from_name;
  char* subject;
  char* body;
  char* to;
  char* to_name;
} m_body;

typedef struct config {
  m_setting *setting;
  m_body *body;
} cfg;

typedef  void (*parser)(const char *, cfg*);

void parse_configuration(const char *ininame, cfg* cfg) {
  dictionary *ini;

  ini = iniparser_load(ininame);
  if (ini == NULL) {
    fprintf(stderr, "cannot parse file: %s\n", ininame);
    exit(1);
  }
  iniparser_dump(ini, stdout);

  cfg->setting->port = strdup(iniparser_getstring(ini, "setting:port", "587"));
  cfg->setting->server = strdup(iniparser_getstring(ini, "setting:server", "mail.example.com"));
  cfg->setting->connection_security = iniparser_getint(ini, "setting:conn_security", 1);
  cfg->setting->mail_flag = SMTP_DEBUG | SMTP_NO_CERT_VERIFY;
  cfg->setting->auth = (enum smtp_authentication_method)iniparser_getint(
      ini, "setting:auth", SMTP_AUTH_PLAIN);
  cfg->setting->user = strdup(iniparser_getstring(ini, "setting:user", "mail@example.com"));
  cfg->setting->pass = strdup(iniparser_getstring(ini, "setting:pass", "pass"));
  cfg->body->body = strdup(iniparser_getstring(
      ini, "body:body", "This is an SMTP client library written in C \
    which can get included directly into another program."));
  cfg->body->from = strdup(iniparser_getstring(ini, "body:from", "from@example.com"));
  cfg->body->from_name = strdup(iniparser_getstring(ini, "body:from_name", "fromName"));
  cfg->body->to = strdup(iniparser_getstring(ini, "body:to", "to@example.com"));
  cfg->body->to_name = strdup(iniparser_getstring(ini, "body:to_name", "toName"));
  
  
  iniparser_freedict(ini);
};


void send_mail(cfg *cfg) {
  struct smtp *smtp;
  enum smtp_status_code ret;
  smtp_open(cfg->setting->server, cfg->setting->port,
                  cfg->setting->connection_security, cfg->setting->mail_flag,
                  NULL, &smtp);

  smtp_auth(smtp, cfg->setting->auth, cfg->setting->user,
                  cfg->setting->pass);

  smtp_address_add(smtp, SMTP_ADDRESS_FROM, cfg->body->from,
                         cfg->body->from_name);

  smtp_address_add(smtp, SMTP_ADDRESS_TO, cfg->body->to,
                         cfg->body->to_name);

  smtp_header_add(smtp, "Subject", cfg->body->subject);
  smtp_mail(smtp, cfg->body->body);
  smtp_header_add(smtp,
                  "Content-Type",
                  "text/html");
  ret = smtp_close(smtp);
  if (ret != SMTP_STATUS_OK) {
    fprintf(stderr, "smtp failed: %s\n", smtp_status_code_errstr(ret));
    exit(1);
  }
}


void run(const char* filename){
    cfg* config = (cfg*) malloc(sizeof(cfg));
    config->body = (m_body*)malloc(sizeof(m_body));
    config->setting = (m_setting*)malloc(sizeof(m_setting));
    
    parse_configuration(filename,config);
    send_mail(config);
    free(config->body);
    free(config->setting);
    free(config);
}

int main(int argc, char **argv) { 
    const char* dft = "default.ini";
    if(argc < 2){
        run(dft);
    }else{
        run(argv[1]);
    }
    return 0; 
}