#found this Access Key ID out in the Internet
github_ssh_private_key="-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIBpjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQI5yNCu9T5SnsCAggA
MBQGCCqGSIb3DQMHBAhJISTgOAxtYwSCAWDXK/a1lxHIbRZHud1tfRMR4ROqkmr4
kVGAnfqTyGptZUt3ZtBgrYlFAaZ1z0wxnhmhn3KIbqebI4w0cIL/3tmQ6eBD1Ad1
nSEjUxZCuzTkimXQ88wZLzIS9KHc8GhINiUu5rKWbyvWA13Ykc0w65Ot5MSw3cQc
w1LEDJjTculyDcRQgiRfKH5376qTzukileeTrNebNq+wbhY1kEPAHojercB7d10E
+QcbjJX1Tb1Zangom1qH9t/pepmV0Hn4EMzDs6DS2SWTffTddTY4dQzvksmLkP+J
i8hkFIZwUkWpT9/k7MeklgtTiy0lR/Jj9CxAIQVxP8alLWbIqwCNRApleSmqtitt
Z+NdsuNeTm3iUaPGYSw237tjLyVE6pr0EJqLv7VUClvJvBnH2qhQEtWYB9gvE1dS
BioGu40pXVfjiLqhEKVVVEoHpI32oMkojhCGJs8Oow4bAxkzQFCtuWB1
-----END ENCRYPTED PRIVATE KEY-----"
print ("hello world, ",github_ssh_private_key)

# embedded API credentials
TWITTER_OAUTH_TOKEN = "dkedjekdjekldjekldje"
TWITTER_OAUTH_SECRET = "dkejkdjekdjkejdkjekdjekjdkjed"
AWS_CREDENTIALS = { 'key': 'djekjdkejde', 'secret': 'dncndmncdmncd' }

# reference to internal hosts
LOG_SERVER = "secret.logging.internal.mozilla.com"
r = requests.get("http://some.internal.hosts.that.should.be.hidden")

#python API calls
import commands
template_vars['output'] = commands.getstatusoutput('/usr/bin/process_soemthing')

