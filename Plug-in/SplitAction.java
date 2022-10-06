package com.lsytool;
import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.actionSystem.PlatformDataKeys;
import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.editor.Editor;
import com.intellij.openapi.editor.SelectionModel;
import com.intellij.openapi.ui.Messages;
import com.intellij.openapi.ui.popup.Balloon;
import com.intellij.openapi.ui.popup.JBPopupFactory;
import com.intellij.ui.JBColor;
import com.intellij.util.ui.JBFont;
import org.apache.http.util.TextUtils;
import util.Logger;


import java.awt.*;
import java.lang.reflect.Method;

public class SplitAction extends AnAction {


    @Override
    public void actionPerformed(AnActionEvent e) {
        // TODO: insert action logic here

        //Log 日志初始化
        Logger.init("Split", Logger.DEBUG);

        //获取编辑器
        Editor mEditor = e.getData(PlatformDataKeys.EDITOR);
        if (null == mEditor) {
            Logger.info("mEditor == null");
            return;
        }
        //获取选择器
        SelectionModel model = mEditor.getSelectionModel();

        String selectText = model.getSelectedText();

        if (TextUtils.isEmpty(selectText)) {
            Logger.info("selectText == null");
            return;
        }
        try {
            javapy b = new javapy();
            String final_output = b.split(selectText);
            showPopupBalloon(mEditor,final_output.toString());
        } catch (Exception z) {
            z.printStackTrace();
        }
    }

    private void showPopupBalloon(final Editor editor, final String result) {
        ApplicationManager.getApplication().invokeLater(new Runnable() {
            public void run() {
                JBPopupFactory factory = JBPopupFactory.getInstance();
                factory.createHtmlTextBalloonBuilder(result, null, new JBColor(new Color(186, 238, 186), new Color(73, 117, 73)),null)
                        .setFadeoutTime(5000)
                        .createBalloon()
                        .show(factory.guessBestPopupLocation(editor), Balloon.Position.below);
            }
        });
    }
}

