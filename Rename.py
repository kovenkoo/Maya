#Advance Rename Tools

import maya.cmds as cmds



#Create ReNameTools
def renameTools():
    selection = cmds.ls( sl=1 )
    inputName = cmds.textField('TextInputA', query=True, text=True) 
    
    i = 1
    
    selectionCounts = len(selection)
    selectionCounts = len(str(selectionCounts))        
    
    for obj in selection:
        counts = str(i)
        counts = counts.zfill(selectionCounts)
        
        cmds.rename( obj, inputName + "_" + counts )
    
        i+=1    

#Add Suffix GRP
def QSgrp():
    selection = cmds.ls( sl=1 )
    for addQSgrp in selection:
        cmds.rename( addQSgrp, addQSgrp + '_GRP' )
        
#Add Suffix MOD        
def QSmod():
    selection = cmds.ls( sl=1 )
    for addQSmod in selection:
        cmds.rename( addQSmod, addQSmod + '_MOD' )       
        
        
#Add Suffix LT        
def QSlt():
    selection = cmds.ls( sl=1 )
    for addQSlt in selection:
        cmds.rename( addQSlt, addQSlt + '_LT' )          
        
        
#Add Prefix         
def addPrefix():
    selection = cmds.ls( sl=1 )
    inputPrefixName = cmds.textField('PrefixTextInputA', query=True, text=True)
    for PrefixObj in selection:
        cmds.rename( PrefixObj, inputPrefixName + PrefixObj )         
        
        
#Add Suffix         
def addSuffix():
    selection = cmds.ls( sl=1 )
    inputSuffixName = cmds.textField('SuffixTextInputA', query=True, text=True)
    for SuffixObj in selection:
        cmds.rename( SuffixObj, SuffixObj + inputSuffixName )             


#Delete Last Character
def delLastCharacter():
    selection = cmds.ls( sl=1 )
    for LastNameObj in selection:
        cmds.rename( LastNameObj, LastNameObj[:-1])
    
    
#Delete First Character
def delFirstCharacter():
    selection = cmds.ls( sl=1 )
    for firstNameObj in selection:
        cmds.rename( firstNameObj, firstNameObj[1:])    


#Search and Replace
def SnR():
    SnRall = cmds.ls( transforms=True )
    SnRselected = cmds.ls( sl=True )

    SearchName = cmds.textField('searchTextInput', query=True, text=True)
    ReplaceName = cmds.textField('replaceTextInput', query=True, text=True) 
    
    if cmds.radioButton( 'selectedRBT', query = True, select=True ):    
        for selObj in SnRselected:
            OldName = selObj
            selObj = selObj.replace(SearchName, ReplaceName)
            cmds.rename( OldName, selObj )
    else:
        for SnRa in SnRall:  
            OldName = SnRa
            SnRa = SnRa.replace(SearchName, ReplaceName)
            cmds.rename( OldName, SnRa )           



#Create UI

def kovenRenameUI():
    RNwindow = cmds.window( title="Rename", widthHeight=(228, 500), sizeable=1, minimizeButton=1, maximizeButton=0, resizeToFitChildren=0 )
    cmds.columnLayout( adjustableColumn=False )
    cmds.text(label='Advance Rename Tool by Koven!', w=225, h=35, bgc=(.125,.125,.125))

    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    #Rename Tool Layout
    cmds.frameLayout( label='Rename Tools', borderStyle='in', collapsable=True, width=225 )
    form = cmds.formLayout(height=70, width=225)
    cmds.text('rnTextA', label='Rename : ')
    cmds.textField('TextInputA', width=157)
    cmds.button('BTrename', label='Rename', width=215, bgc=[0.25,0.25,0.25], command='renameTools()')
    cmds.formLayout( form, edit=True, attachPosition=[ ('rnTextA', 'top', 12, 0), ('rnTextA', 'left', 5, 0), ('TextInputA', 'top', 10, 0), ('TextInputA', 'left', 60, 0), ('BTrename', 'top', 40, 0), ('BTrename', 'left', 4, 0)] )

    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    #Prefix-Suffix Layout
    cmds.frameLayout( label='Prefix-Suffix', borderStyle='in', collapsable=True, collapse=True, width=225 )
    formB = cmds.formLayout( height=70 )
    cmds.textField('PrefixTextInputA', text='Prefix_', width=160)
    cmds.button('BTPrefixAdd', label='Add', width=45, command='addPrefix()')
    cmds.textField('SuffixTextInputA', text='_Suffix', width=160)
    cmds.button('BTSuffixA', label='Add', width=45, command='addSuffix()')
    cmds.formLayout( formB, edit=True, attachPosition=[ ('PrefixTextInputA', 'top', 12, 0), ('PrefixTextInputA', 'left', 5, 0), ('BTPrefixAdd', 'top', 10, 0), ('BTPrefixAdd', 'left', 172, 0), ('SuffixTextInputA', 'top', 40, 0), ('SuffixTextInputA', 'left', 5, 0), ('BTSuffixA', 'top', 40, 0), ('BTSuffixA', 'left', 172, 0)] )

    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    #Quick Suffix Layout
    cmds.frameLayout( label='Quick Suffix', borderStyle='in', collapsable=True, collapse=False, width=225 )
    cmds.rowColumnLayout( numberOfColumns=3 )
    cmds.text('emptyA', label='', width=73, height=5)
    cmds.text('emptyB', label='', width=73, height=5)
    cmds.text('emptyc', label='', width=73, height=5)
    cmds.button('BTqsA', label='GRP', width=73, bgc=[0.2,0.2,0.2], command='QSgrp()')
    cmds.button('BTqsB', label='MOD', width=73, bgc=[0.25,0.25,0.25], command='QSmod()')
    cmds.button('BTqsC', label='LT', width=73, bgc=[0.2,0.2,0.2], command='QSlt()')
    cmds.text('emptyD', label='', width=73, height=5)
    cmds.text('emptyE', label='', width=73, height=5)
    cmds.text('emptyF', label='', width=73, height=5)

    cmds.setParent( '..' )
    cmds.setParent( '..' )
        
    #Remove First or Last Character
    cmds.frameLayout('removeFLCLayout', label='Remove First or Last Character', borderStyle='in', collapsable=True, collapse=False, width=225 )
    cmds.rowColumnLayout( numberOfColumns=3, bgc=[0.25,0.25,0.25] )
    cmds.text('emptyA1', label='', width=50, height=5)
    cmds.text('emptyB1', label='', width=85, height=5)
    cmds.text('emptyC1', label='', width=85, height=5)
    cmds.text('TTtext', label='Remove:', width=50)
    cmds.button('BTremoveFirstStr', label='First Character', width=85, bgc=[0.2,0.2,0.2], command='delFirstCharacter()')
    cmds.button('BTremoveLastStr', label='Last Character', width=85, bgc=[0.15,0.15,0.15], command='delLastCharacter()')
    cmds.text('emptyD1', label='', width=50, height=5)
    cmds.text('emptyE1', label='', width=85, height=5)  
    cmds.text('emptyF1', label='', width=85, height=5)  
    
    cmds.setParent( '..' )
    cmds.setParent( '..' )          
    
    #Search and Replace Layout
    cmds.frameLayout('SnRLayout', label='Search and Replace', borderStyle='in', collapsable=True, collapse=True, width=225 )
    formC = cmds.formLayout(height=135, width=225)
    cmds.text('searchTextA', label='Search  : ')
    cmds.textField('searchTextInput', width=157)
    cmds.text('replaceTextA', label='Replace : ')
    cmds.textField('replaceTextInput', width=157)
    cmds.radioCollection()
    cmds.radioButton('allRBT', label='All')
    cmds.radioButton('selectedRBT', label='Selected', select=True )
    cmds.button('BTapply', label='Apply', width=215, bgc=[0.25,0.25,0.25], command='SnR()')
    cmds.formLayout( formC, edit=True, attachPosition=[ ('searchTextA', 'top', 12, 0), ('searchTextA', 'left', 5, 0), ('searchTextInput', 'top', 10, 0), ('searchTextInput', 'left', 60, 0), ('replaceTextA', 'top', 40, 0), ('replaceTextA', 'left', 4, 0), ('replaceTextInput', 'top', 40, 0), ('replaceTextInput', 'left', 60, 0), ('allRBT', 'top', 70, 0), ('allRBT', 'left', 50, 0), ('selectedRBT', 'top', 70, 0), ('selectedRBT', 'left', 110, 0), ('BTapply', 'top', 100, 0), ('BTapply', 'left', 5, 0) ] )
     
    cmds.showWindow( RNwindow )
    
        
#Open UI

if __name__ == '__main__':
    kovenRenameUI()