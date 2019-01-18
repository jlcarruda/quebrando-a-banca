
import pandas as pd
import json

def start():
    arqSaida = open('saida.txt', "w")
    bestCombination={}

    lol_df = pd.read_csv('./datasets/LeagueofLegends.csv', thousands=",")
    dic_bResult          = ((lol_df[['bResult']]).to_json())
    dic_blueTopChamp     = ((lol_df[['blueTopChamp']]).to_json())
    dic_blueMiddleChamp  = ((lol_df[['blueMiddleChamp']]).to_json())
    dic_blueJungleChamp  = ((lol_df[['blueJungleChamp']]).to_json())
    dic_blueSupportChamp = ((lol_df[['blueSupportChamp']]).to_json())
    dic_blueADCChamp     = ((lol_df[['blueADCChamp']]).to_json())
    dic_year             = ((lol_df[['Year']]).to_json())
    dic_season           = ((lol_df[['Season']]).to_json())


    dic_rResult          = ((lol_df[['rResult']]).to_json())
    dic_redTopChamp     = ((lol_df[['redTopChamp']]).to_json())
    dic_redMiddleChamp  = ((lol_df[['redMiddleChamp']]).to_json())
    dic_redJungleChamp  = ((lol_df[['redJungleChamp']]).to_json())
    dic_redSupportChamp = ((lol_df[['redSupportChamp']]).to_json())
    dic_redADCChamp     = ((lol_df[['redADCChamp']]).to_json())
    dic_year             = ((lol_df[['Year']]).to_json())
    dic_season           = ((lol_df[['Season']]).to_json())

    dicbResult          = json.loads(dic_bResult)
    dicblueTopChamp     = json.loads(dic_blueTopChamp)
    dicblueMiddleChamp  = json.loads(dic_blueMiddleChamp)
    dicblueJungleChamp  = json.loads(dic_blueJungleChamp)
    dicblueSupportChamp = json.loads(dic_blueSupportChamp)
    dicblueADCChamp     = json.loads(dic_blueADCChamp)
    dicyear             = json.loads(dic_year)
    dicseason           = json.loads(dic_season)


    dicrResult          = json.loads(dic_rResult)
    dicredTopChamp     = json.loads(dic_redTopChamp)
    dicredMiddleChamp  = json.loads(dic_redMiddleChamp)
    dicredJungleChamp  = json.loads(dic_redJungleChamp)
    dicredSupportChamp = json.loads(dic_redSupportChamp)
    dicredADCChamp     = json.loads(dic_redADCChamp)
    dicyear             = json.loads(dic_year)
    dicseason           = json.loads(dic_season)

        
        

    for x in range(0,len(dicbResult['bResult'])):
        
        if dicbResult['bResult'][str(x)]==1:
            try:
                dictonary=bestCombination["Blue,"+str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Blue,"+str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Blue,"+str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicblueTopChamp['blueTopChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicblueJungleChamp['blueJungleChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Blue'
            try:
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicblueJungleChamp['blueJungleChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Blue'
            try:
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicblueJungleChamp['blueJungleChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicblueSupportChamp['blueSupportChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Blue'
            try:
                dictonary=bestCombination["Blue,"+str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Blue,"+str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Blue,"+str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicblueADCChamp['blueADCChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicblueSupportChamp['blueSupportChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Blue'
            
        else:
            try:
                dictonary=bestCombination["Blue,"+str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['DEFEAT']        +=1
                dictonary['TOTALPLAYED']   +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']
                
            
                    
                    
            except:
                dictonary=bestCombination["Blue,"+str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Blue,"+str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicblueTopChamp['blueTopChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicblueJungleChamp['blueJungleChamp'][str(x)])
                dictonary['VICTORY']        =0
                dictonary['DEFEAT']         =1 
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =0.0
                dictonary['PERCENTDEFEAT']  =1.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Blue'
            try:
                dictonary=bestCombination[str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicblueJungleChamp['blueJungleChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Blue'
            try:
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicblueJungleChamp['blueJungleChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicblueSupportChamp['blueSupportChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Blue'
            try:
                dictonary=bestCombination["Blue,"+str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Blue,"+str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Blue,"+str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicblueADCChamp['blueADCChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicblueSupportChamp['blueSupportChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Blue'
                    

        if dicrResult['rResult'][str(x)]==1:
            try:
                dictonary=bestCombination["Red,"+str(dicredTopChamp['redTopChamp'][str(x)])+","+str(dicredJungleChamp['redJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Red,"+str(dicredTopChamp['redTopChamp'][str(x)])+","+str(dicredJungleChamp['redJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Red,"+str(dicredTopChamp['redTopChamp'][str(x)])+","+str(dicredJungleChamp['redJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicredTopChamp['redTopChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicredJungleChamp['redJungleChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Red'
            try:
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredMiddleChamp['redMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredMiddleChamp['redMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredMiddleChamp['redMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicredJungleChamp['redJungleChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicredMiddleChamp['redMiddleChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Red'
            try:
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicredJungleChamp['redJungleChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicredSupportChamp['redSupportChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Red'
            try:
                dictonary=bestCombination["Red,"+str(dicredADCChamp['redADCChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Red,"+str(dicredADCChamp['redADCChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Red,"+str(dicredADCChamp['redADCChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicredADCChamp['redADCChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicredSupportChamp['redSupportChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Red'
            
        else:
            try:
                dictonary=bestCombination["Red,"+str(dicredTopChamp['redTopChamp'][str(x)])+","+str(dicredJungleChamp['redJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['DEFEAT']        +=1
                dictonary['TOTALPLAYED']   +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']
            
                    
                    
            except:
                dictonary=bestCombination["Red,"+str(dicredTopChamp['redTopChamp'][str(x)])+","+str(dicredJungleChamp['redJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Red,"+str(dicredTopChamp['redTopChamp'][str(x)])+","+str(dicredJungleChamp['redJungleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicredTopChamp['redTopChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicredJungleChamp['redJungleChamp'][str(x)])
                dictonary['VICTORY']        =0
                dictonary['DEFEAT']         =1 
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =0.0
                dictonary['PERCENTDEFEAT']  =1.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Red'
            try:
                dictonary=bestCombination[sRr(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredMiddleChamp['redMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredMiddleChamp['redMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredMiddleChamp['redMiddleChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicredJungleChamp['redJungleChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicredMiddleChamp['redMiddleChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Red'
            try:
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicredJungleChamp['redJungleChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicredSupportChamp['redSupportChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Red'
            try:
                dictonary=bestCombination["Red,"+str(dicredADCChamp['redADCChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['VICTORY']        +=1
                dictonary['TOTALPLAYED']    +=1
                dictonary['PERCENTVICTORY'] =dictonary['VICTORY']/dictonary['TOTALPLAYED']
                dictonary['PERCENTDEFEAT']  =dictonary['DEFEAT']/dictonary['TOTALPLAYED']

                    
                    
            except:
                dictonary=bestCombination["Red,"+str(dicredADCChamp['redADCChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]={}
                dictonary=bestCombination["Red,"+str(dicredADCChamp['redADCChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+','+str(dicyear['Year'][str(x)])+','+str(dicseason['Season'][str(x)])]
                dictonary['CHAMP1']         =str(dicredADCChamp['redADCChamp'][str(x)])
                dictonary['CHAMP2']         =str(dicredSupportChamp['redSupportChamp'][str(x)])
                dictonary['VICTORY']        =1
                dictonary['DEFEAT']         =0
                dictonary['TOTALPLAYED']    =1
                dictonary['PERCENTVICTORY'] =1.0
                dictonary['PERCENTDEFEAT']  =0.0
                dictonary['YEAR']           =str(dicyear['Year'][str(x)])
                dictonary['SEASON']         =str(dicseason['Season'][str(x)])
                dictonary['TEAM']           ='Red'
                    



    arqSaida.write(str(bestCombination))
