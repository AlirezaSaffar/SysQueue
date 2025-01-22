// import QtQuick 2.15
// import QtQuick.Controls 2.15
// import Pyside_handler 1.0
// import QtQuick.Layouts

// ApplicationWindow {
//     visible: true
//     width: 600
//     height: 600

//     Monitor {
//         id: monitor_pyside
//     }
//     ColumnLayout {
//         x :100
//         y: 100
//         spacing: 0 // Add spacing between rows
//         width: parent.width
//         height: parent.height
//         Rectangle {
//             height: parent.height / 4
//             color: "#000000"
//             width: parent.width
//         }

//         // CPU1 Row
//         RowLayout {
//             Layout.fillWidth: true
//             Layout.preferredHeight: parent.height / 12

//             Text {
//                 text: "CPU1"
//                 font.pixelSize: 16
//                 Layout.alignment: Qt.AlignVCenter
//                 Layout.preferredWidth: parent.width / 6
//             }

//             ProgressBar {
//                 Layout.fillWidth: true
//                 id: sys1
//             }
//         }

//         // CPU2 Row
//         RowLayout {
//             Layout.fillWidth: true
//             Layout.preferredHeight: parent.height / 12

//             Text {
//                 text: "CPU2"
//                 font.pixelSize: 16
//                 Layout.alignment: Qt.AlignVCenter
//                 Layout.preferredWidth: parent.width / 6
//             }

//             ProgressBar {
//                 Layout.fillWidth: true
//                 id: sys2
//             }
//         }

//         // CPU3 Row
//         RowLayout {
//             Layout.fillWidth: true
//             Layout.preferredHeight: parent.height / 12

//             Text {
//                 text: "CPU3"
//                 font.pixelSize: 16
//                 Layout.alignment: Qt.AlignVCenter
//                 Layout.preferredWidth: parent.width / 6
//             }

//             ProgressBar {
//                 Layout.fillWidth: true
//                 id: sys3
//             }
//         }
//     }

// }
import QtQuick 2.15
import QtQuick.Controls 2.15
import Pyside_handler 1.0
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 600
    height: 600
    title: "CPU Monitor"

    Monitor {
        id: monitor_pyside
    }

    Rectangle {
        anchors.fill: parent
        anchors.margins: 20 // Adds spacing from the page borders
        color: "#f5f5f5" // Light gray background for contrast

        ColumnLayout {
            anchors.fill: parent
            spacing: 10 // Add spacing between rows

            // Header Rectangle
            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 4
                color: "lightblue"

                Text {
                    anchors.centerIn: parent
                    text: "RT Scheduling, Afshar-Safar"
                    font.pixelSize: 24
                    font.bold: true
                    color: "#000000"
                }
            }

            // CPU1 Row
            RowLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 12
                spacing: 10 // Space between text and progress bar

                Text {
                    text: "CPU1"
                    font.pixelSize: 16
                    Layout.alignment: Qt.AlignVCenter
                    Layout.preferredWidth: parent.width / 6
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                }

                ProgressBar {
                    Layout.fillWidth: true
                    id: sys1
                }
            }

            // CPU2 Row
            RowLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 12
                spacing: 10

                Text {
                    text: "CPU2"
                    font.pixelSize: 16
                    Layout.alignment: Qt.AlignVCenter
                    Layout.preferredWidth: parent.width / 6
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                }

                ProgressBar {
                    Layout.fillWidth: true
                    id: sys2
                }
            }

            // CPU3 Row
            RowLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 12
                spacing: 10

                Text {
                    text: "CPU3"
                    font.pixelSize: 16
                    Layout.alignment: Qt.AlignVCenter
                    Layout.preferredWidth: parent.width / 6
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                }

                ProgressBar {
                    Layout.fillWidth: true
                    value: 0.5
                    id: sys3
                }
            }
        }
    }
}
