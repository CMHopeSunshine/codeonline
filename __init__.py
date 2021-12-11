import hoshino
from . import *
from .run import *

HELP_MSG = '''
1.[#code [语言] (-i) (输入) 代码] :在线运行代码
'''
sv = hoshino.Service('code', bundle='详细', help_=HELP_MSG)

@sv.on_prefix('#code')
async def code(bot, ev):
  code = ev.message.extract_plain_text().split(' ',1)
  res = await run(code)
  res = '代码运行结果：\n' + res
  await bot.send(ev, res, at_sender=True)
