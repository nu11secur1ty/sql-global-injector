#-*- coding: utf-8 -*-
from os import getcwd as pth
from .tmp import color as _
import requests,re

class sqli_scan(object):
                                                  
      @property
      def error(self):
          return {'Syntax error' : 'Syntax error',
                  'Not found' : 'Not found',
                  'Server Error' : 'Server Error',
                  'Error Occurred While Processing Request':'Error Occurred While Processing Request',
                  "ZIMBRA-WEB-MAIL-01":"zimbra_user",
                  "ZIMBRA-WEB-MAIL-02":"zimbra_ldap_password",
                  "ZIMBRA-WEB-MAIL-03":"ldap_replication_password",
                  "ZIMBRA-WEB-MAIL-04":"ldap_root_password",
                  "ZIMBRA-WEB-MAIL-05":"ldap_nginx_password",
                  "ZIMBRA-WEB-MAIL-06":"mailboxd_keystore_password",
                  "ZIMBRA-WEB-MAIL-07":"zimbra_mysql_password",
                  "ZIMBRA-WEB-MAIL-08":"zimbra_root_password",
                  "ZIMBRA-WEB-MAIL-09":'mysql_root_password',
                  "ZIMBRA-WEB-MAIL-10":'mailboxd_truststore_password',
                  "ZIMBRA-WEB-MAIL-11":'ldap_postfix_password',
                  "ZIMBRA-WEB-MAIL-12":'ldap_amavis_password',
                  "MARIA-DB":'MariaDB server version for the right syntax',
                  "MYSQL-01":'You have an error in your SQL syntax;',
                  "MYSQL-02":'Warning: mysql_',
                  "MYSQL-03":'function.mysql',
                  "MYSQL-04":'MySQL result index', 
                  "MYSQL-05":'MySQL Error',
                  "MYSQL-06":'MySQL ODBC',
                  "MYSQL-07":'MySQL Driver',
                  "MYSQL-08":'mysqli.query',
                  "MYSQL-09":'num_rows',
                  "MYSQL-10":'mysql error:',
                  "MYSQL-11":'supplied argument is not a valid MySQL result resource',
                  "MYSQL-12":'on MySQL result index',
                  "MYSQL-13":'Error Executing Database Query',
                  "MYSQL-14":'mysql_',
                  "MYSQL-15":'mysql_fetch_array\(\)',
                  "MYSQL-16":'mysql_fetch',
                  "MICROSOFT-01":'Microsoft JET Database',
                  "MICROSOFT-02":'ADODB.Recordset', 
                  "MICROSOFT-03":'Unclosed quotation mark',
                  "MICROSOFT-04":'500 - Internal server error',
                  "MICROSOFT-05":'Microsoft OLE DB Provider',
                  "MICROSOFT-06":'Unclosed quotes',
                  "MICROSOFT-07":'ADODB.Command', 
                  "MICROSOFT-08":'ADODB.Field error',
                  "MICROSOFT-09":'Microsoft VBScript',
                  "MICROSOFT-10":'Microsoft OLE DB Provider for SQL Server',
                  "MICROSOFT-11":'Unclosed quotation mark',
                  "MICROSOFT-12":'Microsoft OLE DB Provider for Oracle',
                  "MICROSOFT-13":'Active Server Pages error',
                  "MICROSOFT-14":'OLE/DB provider returned message',
                  "MICROSOFT-15":'OLE DB Provider for ODBC',  
                  "MICROSOFT-16":"error '800a0d5d'",
                  "MICROSOFT-17":"error '800a000d'", 
                  "MICROSOFT-18":'Unclosed quotation mark after the character string', 
                  "MICROSOFT-19":'\[Microsoft\]\[SQL Server Native Client 11.0\]\[SQL Server\]',
                  "MICROSOFT-20":'Warning: odbc_',
                  "ORACLE-01":'ORA-00921: unexpected end of SQL command',
                  "ORACLE-02":'ORA-01756',
                  "ORACLE-03":'ORA-',
                  "ORACLE-04":'Oracle ODBC',
                  "ORACLE-05":'Oracle Error',
                  "ORACLE-06":'Oracle Driver',
                  "ORACLE-07":'Oracle DB2',
                  "ORACLE-08":'Error ORA-',
                  "ORACLE-09":'SQL command not properly ended',
                  "DB2-01":"DB2 ODBC",
                  "DB2-02":"DB2 error",
                  "DB2-03":"Driver",
                  "ODBC-01":"ODBC SQL",
                  "ODBC-02":"ODBC DB2",
                  "ODBC-03":"ODBC Driver",
                  "ODBC-05":"Microsoft Access",
                  "ODBC-06":"Oracle",
                  "ODBC-07":"Microsoft Access Driver",
                  "ODBC-08":'OLE DB Provider for ODBC',
                  "POSTGRESQL-01":'Warning: pg_',
                  "POSTGRESQL-02":"PostgreSql Error:",
                  "POSTGRESQL-03":"function.pg",
                  "POSTGRESQL-04":'Supplied argument is not a valid PostgreSQL result',
                  "POSTGRESQL-05":'PostgreSQL query failed: ERROR: parser: parse error',
                  "POSTGRESQL-06":"pg_",
                  "SYBASE-01":'Warning: sybase_',             
                  "SYBASE-02":'function\.sybase',
                  "SYBASE-03":'Sybase result index',             
                  "SYBASE-04":'Sybase Error:',
                  "SYBASE-05":'Sybase: Server message:',
                  "SYBASE-06":'\[Sybase\]\[ODBC Driver\]:',
                  "SYBASE-07":"sybase_",
                  "JDBC_CFM-01":'Error Executing Database Query',             
                  "JDBC_CFM-02":'SQLServer JDBC Driver',
                  "JDBC_CFM-03":'JDBC SQL',
                  "JDBC_CFM-04":'JDBC Oracle',
                  "JDBC_CFM-05":'JDBC MySQL',
                  "JDBC_CFM-06":"JDBC Error",
                  "JDBC_CFM-07":"JDBC Driver",                           
                  'Not found' : 'Not found',
                  "PHP-ERROR-01":'Warning: include',
                  "PHP-ERROR-02":'Fatal error: include',
                  "PHP-ERROR-03":'Warning: require',
                  "PHP-ERROR-04":'Fatal error: require',
                  "PHP-ERROR-05":'ADODB_Exce2ption',              
                  "PHP-ERROR-06":'Warning: include\(',
                  "PHP-ERROR-07":'Warning: require_once\(',
                  "PHP-ERROR-08":'function.include',
                  "PHP-ERROR-09":'Disallowed Parent Path',
                  "PHP-ERROR-10":'function.require',
                  "PHP-ERROR-11":'Warning: main\(',
                  "PHP-ERROR-12":'Warning: session_start\(\)',
                  "PHP-ERROR-13":'Warning: getimagesize\(\)',
                  "PHP-ERROR-14":'Warning: array_merge\(\)',
                  "PHP-ERROR-15":'Warning: preg_match\(\)',
                  "PHP-ERROR-16":'GetArray\(\)',
                  "PHP-ERROR-17":'FetchRow\(\)',
                  "PHP-ERROR-18":'Warning: preg_',
                  "PHP-ERROR-19":'Warning: ociexecute\(\)',                       
                  "PHP-ERROR-20":'Warning: ocifetchstatement\(\)',
                  "ASP-ERROR-01":'Version Information: Microsoft \.NET Framework',
                  "ASP-ERROR-02":'ASP.NET is configured to show verbose error messages',
                  "ASP-ERROR-03":"BOF or EOF",
                  "ASP-ERROR-04":'Unclosed quotation mark',
                  "ASP-ERROR-05":'Error converting data type varchar to numeric',
                  "INDEFINITE-01":'Input string was not in a correct format',
                  "INDEFINITE-02":'An illegal character has been found in the statement',
                  "INDEFINITE-03":"Invalid Querystring",
                  "INDEFINITE-04":"Fatal error",
                  "INDEFINITE-05":"Incorrect syntax near",
                  "BASE-TEST":"'",}
                  
      def scan(self,url):
          self.url = url
          _vuln = 0
          __vuln = ""
          resp = requests.get(f"{self.url}'").text
          for a,b in self.error.items():
              if re.search(b,resp):
                 f = open(f'{pth()}/vuln.txt','a+')
                 f.write(f'{self.url}\n')
                 f.close()
                 _vuln += 1
                 __vuln += b
              else:
                 pass
          
          if _vuln > 0:
             print('\n')
             print(f'{_.G}[!]{_.W} Vulnerability SQLi')
             print(f'{_.Y}[E]{_.W} : {__vuln}')
             print(f'{_.B}[URL]{_.W} : {self.url}')
             print(f'Save To : {pth()}/vuln.txt')
             print('\n')
          else:
             print(f'{_.R}[-]{_.W} Not Vulnerability')
             print(f'{_.B}[URL]{_.W} : {self.url}')
