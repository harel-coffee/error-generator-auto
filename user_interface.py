from methodss.typos.typo_keyboard.typo_keyboard import Typo_Keyboard
from methodss.typos.typo_butterfingers.typo_butterfingers import Typo_Butterfingers
from methodss.switch_value.random_active_domain.random_active_domain import Random_Active_Domain
from methodss.switch_value.Similar_based_active_domain.similar_based_active_domain import Similar_Based_Active_Domain
from methodss.noise.white_noise.white_noise import White_Noise
from methodss.noise.gaussian_noise.gaussian_noise import Gaussian_Noise
from methodss.missing_value.implicit_missing_value.implicit_missing_value import Implicit_Missing_Value
from methodss.missing_value.explicit_missing_value.explicit_missing_value import Explicit_Missing_Value
from methodss.word2vec.word2vec_nearest_neighbor.word2vec_nearest_neighbor import Word2vec_Nearest_Neighbor
from methodss.primary_function.input_output import Read_Write
from methodss.primary_function.list_selected import List_selected
from error_generator_api import Error_Generator


dataset,dataframe = Read_Write.read_csv_dataset("./datasets/test.csv")

# mymethod=Typo_Keyboard()
# mymethod=Typo_Butterfingers()


# mymethod=Similar_Based_Active_Domain()
# mymethod=Random_Active_Domain()


# mymethod=White_Noise()
# mymethod=Gaussian_Noise()

# mymethod=Implicit_Missing_Value()
# mymethod=Explicit_Missing_Value()

mymethod=Word2vec_Nearest_Neighbor()

myselector=List_selected()

mygen=Error_Generator()
new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=50,dataset=dataset)

# write to output
Read_Write.write_csv_dataset("./outputs/{}.csv".format(mymethod.name), new_dataset)
