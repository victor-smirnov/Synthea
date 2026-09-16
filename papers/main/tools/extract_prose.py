import re,sys
D='/home/victor/devel/nous-v0/docs/paper_v2/'
order=['sec1-intro','sec2-background','sec3-account','sec4-model','sec5-transformers','sec7-discussion','sec8-conclusion','sec-appendix']
out=['# What Is It Like to Be a Language Model? (paper v2, prose extracted for encoding)','']
def clean(t):
    t=re.sub(r'(?m)^\s*%.*\n','',t)
    t=re.sub(r'(?<!\\)%.*','',t)
    t=re.sub(r'\\label\{[^}]*\}','',t)
    t=re.sub(r'\\(?:citet|citep|cite|citeauthor|citeyear)(?:\[[^\]]*\])?\{([^}]*)\}',lambda m:' '.join('['+k.strip()+']' for k in m.group(1).split(',')),t)
    t=re.sub(r'\\ref\{([^}]*)\}',r'\1',t)
    t=re.sub(r'\\section\*?\{([^}]*)\}',r'\n## \1\n',t)
    t=re.sub(r'\\subsection\*?\{([^}]*)\}',r'\n### \1\n',t)
    t=re.sub(r'\\subsubsection\*?\{([^}]*)\}',r'\n#### \1\n',t)
    t=re.sub(r'\\paragraph\{([^}]*)\}',r'\n**\1** ',t)
    t=re.sub(r'\\item\s*',r'\n- ',t)
    t=re.sub(r'\\begin\{(?:figure|table|tikzpicture|tabular)[^\n]*\n.*?\\end\{(?:figure|table|tikzpicture|tabular)\}','[figure/table omitted]',t,flags=re.S)
    t=re.sub(r'\\begin\{[^}]*\}(\[[^\]]*\])?','',t); t=re.sub(r'\\end\{[^}]*\}','',t)
    for _ in range(4):
        t=re.sub(r'\\(?:emph|textit|textbf|cyr|cyrfont|footnote|thanks|texttt|mbox|text)\{([^{}]*)\}',r'\1',t)
    t=re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?\{([^{}]*)\}',r'\2',t)
    t=re.sub(r'\\[a-zA-Z]+\s*','',t)
    t=t.replace('``','"').replace("''",'"').replace('~',' ').replace('--','--')
    t=re.sub(r'\{|\}','',t)
    t=re.sub(r'\n{3,}','\n\n',t)
    return t
for f in order:
    out.append(clean(open(D+f+'.tex').read()))
txt='\n'.join(out)
open(D+'paper-prose.md','w').write(txt)
print(len(txt.split()),'words')
