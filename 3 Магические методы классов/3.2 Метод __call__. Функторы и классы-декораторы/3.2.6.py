class RenderList:
    def __init__(self,  type_list):
        self.tl =  type_list if type_list in ('ul', 'ol') else 'ul'
        
    def __call__(self, value, *args, **kwargs):
        return "\n".join([f'<{self.tl}>', *map(lambda x: f"<li>{x}</li>", lst), f'</{self.tl}>'])
                    
        

         


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)