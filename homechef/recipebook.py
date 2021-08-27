from recipe import Recipe

class RecipeBook:

    def __init__(self):
        self.recipe_list = []
        self.init_recipe()

    def add_recipe(self):
        # 추가할 레시피 이름 입력받기
        name = input('>> 레시피 이름을 입력하세요: ')

        # 중복 체크 하기
        for recipe in self.recipe_list:
            # 중복되는 레시피가 있으면
            if name == recipe.name:
                # 중복된다고 알려주기
                print('이미 존재하는 레시피입니다!')
                return # 함수를 끝내겠다는 리턴 추가

        # 중복되는 레시피가 없으면
        # 레시피 생성하기
        new_recipe = Recipe(name)
        new_recipe.set_recipe()
        # 레시피 리스트에 레시피 추가하기
        self.recipe_list.append(new_recipe)

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index+1}')
            print(recipe)

    # 레시피북에서 레시피 찾기
    def search_recipe(self):
        searched_recipe = []
        # 레시피 이름 검색하기 (입력 받기)
        name = input('>> 원하는 레시피를 검색하세요: ')
        # (반복문 시작) 레시피 리스트를 돌면서 찾는 레시피가 있는지 확인하기
        for recipe in self.recipe_list:
            # 찾는 레시피가 있다면 (레시피의 이름이 검색받은 이름과 같다면)
            if name == recipe.name:
                # 있는 레시피 보여주기
                print(recipe)
                searched_recipe.append(recipe)
                
        # 검색된 레시피가 없다면 (searched_recipe 가 비어있다면 )
        if len(searched_recipe) == 0: # 찾아진 레시피의 길이가 0이라면
            # 추가할지 물어보기
            answer = int(input('>> 찾는 레시피가 없습니다. 추가하시겠습니까? (1: 예, 0: 아니요) '))
            # 추가한다고 하면
            if answer == 1: # "if answer" 도 같은말!! 컴퓨터에서는 1을 true 로 생각함
                # 레시피 추가하기
                self.add_recipe()
            else:
                return

    # 재료로 (해당되는) 레시피 찾기
    def search_ingredient(self):
        # 빈 셋(set) 생성 -> 재료를 중복 제거해서 담은 셋(set)
        all_ingredient = set()
        # 레시피븍에 있는 레시피의 재료를 셋(set)이 넣자
        for recipe in self.recipe_list:
            for ingredient in recipe.ingredient:
                all_ingredient.add(ingredient) # 추가
        # 모든 재료를 보여주자
        for index, ingredient in enumerate(all_ingredient):
            print(f'{index+1}. {ingredient}') # index는 0부터 나오니까 사용자에게 1부터 보여주려고 index+1을 하는 것임!
        
        # 찾을 재료 검색하기(입력받기)
        search_num = int(input('>> 사용할 재료를 입력하세요: '))
        search_ingredient = list(all_ingredient)[search_num-1]
        # 레시피 리스트의 레시피 -> 레시피의 재료 살펴보기
        for recipe in self.recipe_list:
            # 입력한 재료가 포함되면
            if search_ingredient in recipe.ingredient:
                # 해당 레시피 모두 보여주기
                print(recipe)

    def init_recipe(self):
        떡볶이 = Recipe('떡볶이')
        떡볶이.people = 2
        떡볶이.video = 'youtube.com'
        떡볶이.ingredient = {'물':'100', '떡':'200', '고추장':'100', '어묵':'100', '양파':'300'}
        self.recipe_list.append(떡볶이)
        카레 = Recipe('카레')
        카레.people = 1
        카레.video = 'youtube.com'
        카레.ingredient = {'카레가루':'50', '감자':'200', '당근':'100'}
        카레.contents = '맛있게 만드세요!'
        self.recipe_list.append(카레)

    # def __str__(self):
    #     pass
